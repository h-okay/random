import os
import random
from pathlib import Path


class Words:  # type: ignore
    @staticmethod
    def __read_file():
        txt_path = os.path.join(Path(__file__).parent, "data", "randomwords.txt")
        with open(txt_path, "r", encoding="utf-8") as file:
            return file.read().split("\n")

    @staticmethod
    def random_word():
        words = Words.__read_file()
        return random.choice(words)
