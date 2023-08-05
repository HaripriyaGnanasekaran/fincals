from model.calculation.base import CalculationNode
from model.calculation.variables.levels import monte_carlo_df, metrics_dict
from model.calculation.variables import computed_variables as cv
from model.calculation.parameters import parameters as p
from model.calculation.variables import domain_values as dv
from scipy.stats import t, norm
import numpy as np
import pandas as pd
from tqdm import tqdm


class PopulateMonteCarloDF(CalculationNode):
    def execute(self):
        n_days = p.business_days_in_year * p.years_to_simulate
        days = list(range(1, n_days + 1))
        degree_of_freedom = self.data[metrics_dict][cv.historical_return_deg_freedom]
        mean = (
            self.data[metrics_dict][cv.historical_return_tmean]
            if p.fit == dv.student_t
            else self.data[metrics_dict][cv.historical_return_mean]
        )
        std = (
            self.data[metrics_dict][cv.historical_return_tstd]
            if p.fit == dv.student_t
            else self.data[metrics_dict][cv.historical_return_std]
        )

        scenario_returns = np.zeros((n_days, p.scenarios))
        for scenario in tqdm(range(p.scenarios), desc="Simulating scenarios"):
            np.random.seed(scenario * 123)
            random_t_returns = self._get_random_returns(
                degree_of_freedom, mean, std, n_days
            )
            cumulative_returns = pd.Series(random_t_returns + 1).cumprod()
            scenario_returns[:, scenario] = (
                cumulative_returns * self.data[metrics_dict][cv.current_stock_price]
            )

        scenario_columns = [f"price_{scenario}" for scenario in range(p.scenarios)]
        self.data[monte_carlo_df] = pd.DataFrame(
            scenario_returns, columns=scenario_columns
        )
        self.data[monte_carlo_df][cv.day] = days
        self.data[monte_carlo_df].set_index([cv.day], inplace=True)

    @staticmethod
    def _get_random_returns(degree_of_freedom, mean, std, n_days):
        if p.fit == dv.student_t:
            return t.rvs(df=degree_of_freedom, loc=mean, scale=std, size=n_days)
        else:
            return norm.rvs(loc=mean, scale=std, size=n_days)
