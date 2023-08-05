import pandas as pd

from .input_parameters import InputParameters
from .daily_return import DailyReturn
from .historical_return_std import HistoricalReturnStd
from .historical_return_mean import HistoricalReturnMean
from .historical_return_t_params import HistoricalReturnTParams
from .current_stock_price import CurrentStockPrice
from .populate_montecarlo_df import PopulateMonteCarloDF
from .value_at_risk import ValueAtRisk
from .mean_total_return import MeanTotalReturn
from .expected_value import ExpectedValue
from model.calculation.parameters import parameters as p
from ...base import CalculationNode
from model.calculation.variables import levels as l
from model.calculation.variables import computed_variables as cv

# sequential node graph
nodes = [
    InputParameters,
    DailyReturn,
    CurrentStockPrice,
    HistoricalReturnMean,
    HistoricalReturnStd,
    HistoricalReturnTParams,
    PopulateMonteCarloDF,
    ValueAtRisk,
    MeanTotalReturn,
    ExpectedValue,
]


class VARMonteCarlo:
    @staticmethod
    def execute():
        for node in nodes:
            node().execute()


class VARMonteCarloYearSweep(CalculationNode):
    def execute(self):
        years = list(range(1, 21))
        var_s, exp_val = [], []

        self.data[l.monte_carlo_year_sweep_df] = pd.DataFrame({"Year": years})

        for year in years:
            p.years_to_simulate = year
            for node in nodes:
                node().execute()
            var_s.append(self.data[l.metrics_dict][cv.value_at_risk])
            exp_val.append(self.data[l.metrics_dict][cv.expected_value])

        self.data[l.monte_carlo_year_sweep_df]["VaR"] = pd.Series(var_s)
        self.data[l.monte_carlo_year_sweep_df]["ExpectedValue"] = pd.Series(exp_val)
