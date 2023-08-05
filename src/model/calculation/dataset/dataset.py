import pandas as pd
from model.calculation.variables import levels as l


class Dataset:
    """Represents a dataset containing various dataframes and dictionaries.

    Attributes:
        data (dict): A dictionary containing different data components of the dataset.

            - `l.financial_df` (pandas.DataFrame): DataFrame holding financial data.
            - `l.market_df` (pandas.DataFrame): DataFrame holding market data.
            - `l.monte_carlo_df` (pandas.DataFrame): DataFrame holding Monte Carlo simulation results.
            - `l.metrics_dict` (dict): Dictionary storing various metrics.

    Note:
        The `l` module from `model.calculation.variables` provides the constant keys used to access
        specific data components in the `data` dictionary.

    Example:
        dataset = Dataset()
        dataset.data[l.financial_df] = financial_data
        dataset.data[l.market_df] = market_data
        dataset.data[l.monte_carlo_df] = monte_carlo_results
        dataset.data[l.metrics_dict] = metrics
    """

    data = {
        l.financial_df: pd.DataFrame(),
        l.market_df: pd.DataFrame(),
        l.monte_carlo_df: pd.DataFrame(),
        l.monte_carlo_year_sweep_df: pd.DataFrame(),
        l.metrics_dict: {},
    }
