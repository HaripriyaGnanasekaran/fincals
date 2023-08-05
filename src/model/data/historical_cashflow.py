import pandas as pd
import numpy as np
from scipy.stats import norm, lognorm
import matplotlib.pyplot as plt

df = pd.read_json("./goog.json", orient="records")

# preprocess
df.rename(columns={"year": "Year", "free_cash_flow": "Free_Cash_Flow"}, inplace=True)
df.set_index("Year", inplace=True)
df.index = pd.to_datetime(df.index, format="%Y")
df["FCF_Change"] = df["Free_Cash_Flow"].pct_change()

# statistical parameters
mu = df["FCF_Change"].dropna().mean()
sigma = df["FCF_Change"].dropna().std()
x = np.linspace(-1, 1.5, 100)
pdf = norm.pdf(x, mu, sigma)


plt.hist(
    df["FCF_Change"],
    bins=20,
    density=True,
    alpha=0.25,
    label="Growth Rate Distribution",
)
plt.plot(x, pdf, "r", label="Normal")
plt.text(-0.9, 1, f"Mean: {mu:.2f}")
plt.text(-0.9, 0.95, f"Standard Deviation: {sigma:.2f}")
plt.title("Growth Rate Distribution vs Normal")
plt.xlabel("Growth Rate")
plt.ylabel("Frequency")
plt.show()
