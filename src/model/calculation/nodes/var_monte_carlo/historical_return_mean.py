from model.calculation.base import CalculationNode
from model.calculation.variables.levels import market_df, metrics_dict
from model.calculation.variables import computed_variables as cv


class HistoricalReturnMean(CalculationNode):
    def execute(self):
        mean = self.data[market_df][cv.daily_return].dropna().mean()
        self.data[metrics_dict].update({cv.historical_return_mean: mean})
