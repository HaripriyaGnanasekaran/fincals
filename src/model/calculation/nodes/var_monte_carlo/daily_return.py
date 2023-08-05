import caching
from model.calculation.base import CalculationNode
import yfinance as yf
from model.calculation.variables.levels import market_df
from model.calculation.variables import computed_variables as cv
from model.calculation.variables import existing_variables as ev
from model.calculation.variables import inputs as i


class DailyReturn(CalculationNode):
    def execute(self):
        with caching.Cache(expiration_time=3600):
            self.data[market_df] = yf.download(tickers=i.pltr, progress=False)
            self.data[market_df][cv.daily_return] = self.data[market_df][
                ev.close
            ].pct_change()
