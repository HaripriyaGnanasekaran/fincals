from model.calculation.base import CalculationNode
from model.calculation.variables.levels import metrics_dict
from model.calculation.variables import computed_variables as cv
from model.calculation.parameters import parameters as p


class InputParameters(CalculationNode):
    def execute(self):
        inputs = {
            cv.current_value: p.current_value,
            cv.fit: p.fit,
            cv.years_to_simulate: p.years_to_simulate,
            cv.business_days_in_year: p.business_days_in_year,
            cv.scenarios: p.scenarios,
        }

        for key, value in inputs.items():
            self.data[metrics_dict][key] = value
