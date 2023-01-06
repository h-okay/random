from typing import Tuple

import pandas as pd


class Outliers:
    @staticmethod
    def outlier_thresholds(
        dataframe: pd.DataFrame, variable: str
    ) -> Tuple[float, float]:
        quartile1 = dataframe[variable].quantile(0.01)
        quartile3 = dataframe[variable].quantile(0.99)
        interquantile_range = quartile3 - quartile1
        up_limit = quartile3 + 1.5 * interquantile_range
        low_limit = quartile1 - 1.5 * interquantile_range
        return low_limit, up_limit

    def replace_with_thresholds(self, dataframe: pd.DataFrame, variable: str) -> None:
        low_limit, up_limit = Outliers.outlier_thresholds(dataframe, variable)
        dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
        dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit
        return self

    def drop_negatives(self, dataframe: pd.DataFrame, col: str) -> None:
        if isinstance(col, str):
            dataframe = dataframe[(dataframe[col] > 0)]
        if isinstance(col, list):
            for clm in col:
                self.drop_negatives(dataframe, clm)
        return self

    def drop_contains(self, dataframe: pd.DataFrame, col: str, value: str) -> None:
        dataframe = dataframe[~dataframe[col].str.contains(value, na=False)]
        dataframe = dataframe[dataframe.StockCode != "POST"]
        return self

    def filter_country(self, dataframe: pd.DataFrame, country: str) -> None:
        dataframe = dataframe[dataframe["Country"] == country]
        return self
