import numpy as np
import pandas as pd
import yfinance as yf
import math

start = 2023
cf = 60.01
g = 0.35
r = 0.1375
lg = 0.0211
outstanding_equity = 12781000000

year = list(np.linspace(start, 2032, 10))

# linear growth decay to lg
# g(x) = g - 0.030*n
# g(t) = 0.35*e^(-0.246*t)i
cash_flow = [
    cf * (1 + (g * math.exp(-0.246 * n)) / 2 + (g - 0.008 * n) / 2) ** n
    for n in range(1, 11)
]

df = pd.DataFrame({"Year": year, "Cash": cash_flow}).set_index("Year")
df["N"] = df.index - start
df.loc[2033] = {"N": 10, "Cash": df["Cash"].iloc[-1] * (1 + g) / (r - lg)}
df["Present_Value"] = df["Cash"] / (1 + r) ** df["N"]


fair_value = df["Present_Value"].sum() * 1e9

print(df)
print(f"Fair value of equity: {fair_value/outstanding_equity:0.2f}")
