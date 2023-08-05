import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class ReadHistoricalData:
    def __init__(self, file):
        self.file = file
        self.df = self.read()

    def read(self):
        return pd.read_excel(self.file).set_index("Dates")

    def get(self, column):
        """
        Args:
            column (str): Retrieves the column from historical dataset.
        """

        return self.df[column] if column in self.df.columns else self.process(column)

    def process(self, column):
        if column == "Free_Cash_Flow":
            self.df[column] = (
                self.df["Cash Flow From Operating Activities"]
                + self.df["Net Change In Property Plant And Equipment"]
            )
            return self.df[[column]]


if __name__ == "__main__":
    data = ReadHistoricalData("./AMZN.xlsx")
    free_cash_flow = data.get("Free_Cash_Flow")

    # plot free cash flow
    free_cash_flow.index = pd.to_datetime(free_cash_flow.index)
    free_cash_flow.sort_index(inplace=True)

    free_cash_flow["FCF_Change"] = free_cash_flow["Free_Cash_Flow"].pct_change()
    print(free_cash_flow["FCF_Change"].mean())
    # statistical parameters
    mu = free_cash_flow["FCF_Change"].dropna().mean()
    sigma = free_cash_flow["FCF_Change"].dropna().std()
    x = np.linspace(-1, 1.5, 100)
    pdf = norm.pdf(x, mu, sigma)

    plt.hist(
        free_cash_flow["FCF_Change"],
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
