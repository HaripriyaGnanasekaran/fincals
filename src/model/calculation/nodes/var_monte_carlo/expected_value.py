from model.calculation.base import CalculationNode
from model.calculation.variables.levels import metrics_dict, monte_carlo_df
from model.calculation.variables import computed_variables as cv


class ExpectedValue(CalculationNode):
    def execute(self):
        self.data[metrics_dict][cv.expected_value] = (
            self.data[metrics_dict][cv.current_value]
            * self.data[metrics_dict][cv.mean_total_return]
        )
