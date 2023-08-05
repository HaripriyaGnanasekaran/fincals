from model.calculation.base import CalculationNode
from model.calculation.variables.levels import market_df, metrics_dict
from model.calculation.variables import computed_variables as cv
import numpy as np
from scipy.stats import norm, t, lognorm
import matplotlib.pyplot as plt


class HistoricalReturnStd(CalculationNode):
    def execute(self):
        std = self.data[market_df][cv.daily_return].std()
        self.data[metrics_dict].update({cv.historical_return_std: std})

    def plot(self):
        dr = self.data[market_df][cv.daily_return].dropna()
        x = np.linspace(-0.05, 0.05, 100)
        t_params = t.fit(dr)
        log_norm_params = lognorm.fit(dr)
        print(t_params)

        plt.hist(
            self.data[market_df][cv.daily_return],
            bins=1000,
            density=True,
            alpha=0.9,
            label="Daily return",
        )
        # plt.plot(x, pdf, 'r', label="Normal")
        plt.plot(x, t.pdf(x, *t_params), label="Student's t-distribution")
        plt.plot(x, lognorm.pdf(x, *log_norm_params), label="Log-normal distribution")
        plt.xlabel("Daily return")
        plt.ylabel("Frequency")
        plt.show()
