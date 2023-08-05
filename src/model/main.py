import time
from model.calculation import Calculation
from model.calculation.dataset.dataset import Dataset as d
from model.calculation.variables.levels import metrics_dict
from model.calculation.variables import levels as l
import matplotlib.pyplot as plt
import numpy as np

start = time.time()
Calculation.execute()
end = time.time()

print(f"Finished: Took {(end-start):.2f} seconds.")

financial_metrics = d.data[metrics_dict]

for key, value in financial_metrics.items():
    print(f"{key} = {value}")

df = d.data[l.monte_carlo_df]
columns = np.random.choice(df.columns.to_list(), size=10, replace=False)

plt.plot(df.index, df[df.columns])
plt.yscale("log")
plt.xlabel("Year")
plt.ylabel("Expected Value")
plt.show()
