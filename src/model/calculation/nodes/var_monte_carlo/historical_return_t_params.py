from model.calculation.base import CalculationNode
from model.calculation.variables.levels import market_df, metrics_dict
from model.calculation.variables import computed_variables as cv
from scipy.stats import t


class HistoricalReturnTParams(CalculationNode):
    def execute(self):
        dr = self.data[market_df][cv.daily_return].dropna()
        (df, tmean, tstd) = t.fit(dr)
        self.data[metrics_dict].update({cv.historical_return_deg_freedom: df})
        self.data[metrics_dict].update({cv.historical_return_tmean: tmean})
        self.data[metrics_dict].update({cv.historical_return_tstd: tstd})
