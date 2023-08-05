import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbols and number of years
tickerSymbol_GOOG = "GOOGL"
tickerSymbol_SP500 = "^GSPC"
num_years = 10

# Calculate the start and end dates
end_date = pd.Timestamp.today().strftime("%Y-%m-%d")
start_date = (pd.Timestamp.today() - pd.DateOffset(years=num_years)).strftime(
    "%Y-%m-%d"
)

# Get data on the tickers
tickerData_GOOG = yf.Ticker(tickerSymbol_GOOG)
tickerData_SP500 = yf.Ticker(tickerSymbol_SP500)

# Get the historical prices for the tickers
tickerDf_GOOG = tickerData_GOOG.history(period="1d", start=start_date, end=end_date)
tickerDf_SP500 = tickerData_SP500.history(period="1d", start=start_date, end=end_date)

# Calculate the annual returns of the stocks and index
closing_prices_GOOG = tickerDf_GOOG["Close"]
closing_prices_SP500 = tickerDf_SP500["Close"]
annual_returns_GOOG = closing_prices_GOOG.resample("Y").last().pct_change()
annual_returns_SP500 = closing_prices_SP500.resample("Y").last().pct_change()

# Print the annual returns
print(
    "Historical annual returns for",
    tickerSymbol_GOOG,
    "over the past",
    num_years,
    "years:",
)
print(annual_returns_GOOG)

print(
    "Historical annual returns for",
    tickerSymbol_SP500,
    "over the past",
    num_years,
    "years:",
)
print(annual_returns_SP500)

# Calculate the beta of the stock
covariance = np.cov(annual_returns_GOOG.dropna(), annual_returns_SP500.dropna())[0][1]
variance = np.var(annual_returns_SP500.dropna())

beta = covariance / variance

# Print the beta
print("Beta of", tickerSymbol_GOOG, "with respect to", tickerSymbol_SP500, ":", beta)


# discount rate
risk_free_rate = 3.86
discount_rate = risk_free_rate + beta * (10 - risk_free_rate)
print(f"Disount rate for {tickerSymbol_GOOG}: {discount_rate:.2f}")
