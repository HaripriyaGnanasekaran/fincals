from model.calculation.base import CalculationNode
from model.calculation.variables.levels import metrics_dict, monte_carlo_df
from model.calculation.variables import computed_variables as cv


class MeanTotalReturn(CalculationNode):
    def execute(self):
        average_closing_price = self.data[monte_carlo_df].iloc[-1].mean()
        self.data[metrics_dict][cv.mean_total_return] = (
            average_closing_price / self.data[metrics_dict][cv.current_stock_price]
        )
