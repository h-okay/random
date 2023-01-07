import logging
import os
import warnings
from pathlib import Path

import pandas as pd
from helpers import Outliers
from mlxtend.frequent_patterns import apriori, association_rules

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO)


class AssociationRuleLearner:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_data(self):
        from kaggle.api.kaggle_api_extended import \
            KaggleApi  # pylint: disable=import-outside-toplevel, import-error, no-name-in-module

        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(
            dataset="mashlyn/online-retail-ii-uci",
            path=os.path.join(Path(__file__).parent, "data"),
            unzip=True,
            quiet=True,
        )

    def load_data(self):
        self.logger.info("Loading data")
        return pd.read_csv("data/online_retail_II.csv")

    def clean_data(self, df_):
        self.logger.info("Cleaning data")
        out = Outliers()
        (
            out.drop_negatives(df_, ["Quantity", "Price"])
            .drop_contains(df_, "Invoice", "C")
            .filter_country(df_, "United Kingdom")
        )
        return df_

    def create_agg_df(self, df_):
        self.logger.info("Creating aggregated dataframe")
        return (
            df_.groupby(["Invoice", "StockCode"])
            .Quantity.sum()
            .unstack()
            .fillna(0)
            .applymap(lambda x: 1 if x > 0 else 0)
        )

    def rules(self, agg_df_):
        self.logger.info("Running association rule learner")
        freq_sets = apriori(
            agg_df_.astype("bool"), min_support=0.01, use_colnames=True, low_memory=True
        )
        return association_rules(freq_sets, metric="support", min_threshold=0.01)

    def __get_name_from_id(self, df_, id_):
        return str(df_.loc[df_.StockCode == id_].Description.values[0])

    def format_output(self, final_df_, df_):
        self.logger.info("Formatting output")
        final_df_["antecedents"] = final_df_.antecedents.apply(
            lambda x: ", ".join([self.__get_name_from_id(df_, id_) for id_ in x])
        )
        final_df_["consequents"] = final_df_.consequents.apply(
            lambda x: ", ".join([self.__get_name_from_id(df_, id_) for id_ in x])
        )

    def run(self):
        self.get_data()
        data = self.load_data()
        data = self.clean_data(data)
        agg_df = self.create_agg_df(data)
        rules = self.rules(agg_df)
        self.format_output(rules, data)
        rules.to_csv("data/rules.csv", index=False)
        self.logger.info(
            "Rules saved to %s", os.path.join(Path(__file__).parent, "data/rules.csv")
        )
