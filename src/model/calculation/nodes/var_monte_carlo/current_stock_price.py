from src.model.calculation.base import CalculationNode

from src.model.calculation.variables.levels import market_df, metrics_dict
from src.model.calculation.variables import computed_variables as cv
from src.model.calculation.variables import existing_variables as ev


class CurrentStockPrice(CalculationNode):
    def execute(self):
        self.data[metrics_dict].update(
            {cv.current_stock_price: self.data[market_df][ev.close].iloc[-1]}
        )
