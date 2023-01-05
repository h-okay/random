import ast
from typing import Any, Dict, List

import pandas as pd

FILTER = [
    "id",
    "title",
    "genres",
    "belongs_to_collection",
    "vote_average",
    "vote_count",
    "budget",
    "revenue",
    "popularity",
    "production_companies",
    "production_countries",
    "release_date",
    "runtime",
    "spoken_languages",
]
FILL = {"belongs_to_collection": "[{'name':'No'}]"}
UNPACK = [
    "belongs_to_collection",
    "production_companies",
    "production_countries",
    "spoken_languages",
    "genres",
]


class Cleaner:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = pd.DataFrame(data)

    @staticmethod
    def unpacker(text):
        unpack_str = []
        if isinstance(text, list):
            for val in text:
                unpack_str.append(val.get("name"))

        if isinstance(text, dict):
            unpack_str.append(text.get("name"))

        if isinstance(text, str):
            arr = ast.literal_eval(text)
            Cleaner.unpacker(arr)

        return ", ".join(unpack_str)

    def filter_columns(self) -> None:
        self.data = self.data[
            self.data["adult"] == False  # pylint: disable=singleton-comparison
        ]
        self.data = self.data[FILTER]
        self.data = self.data.set_index("id").sort_index()
        return self

    def fill_columns(self) -> None:
        for column, filler in FILL.items():
            self.data[column] = self.data[column].fillna(filler)
        return self

    def unpack_columns(self) -> None:
        for column in UNPACK:
            self.data[column] = self.data[column].apply(Cleaner.unpacker)
        return self
