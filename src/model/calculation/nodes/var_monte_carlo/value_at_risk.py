from model.calculation.base import CalculationNode
from model.calculation.variables.levels import metrics_dict, monte_carlo_df
from model.calculation.variables import computed_variables as cv


class ValueAtRisk(CalculationNode):
    def execute(self):
        five_percentile_value = self.data[monte_carlo_df].iloc[-1].quantile(0.05)
        expected_worst_return = (
            five_percentile_value / self.data[metrics_dict][cv.current_stock_price]
        )
        portfolio_value_lost = self.data[metrics_dict][cv.current_value] * (
            1.0 - expected_worst_return
        )
        self.data[metrics_dict][cv.value_at_risk] = portfolio_value_lost.clip(min=0)
