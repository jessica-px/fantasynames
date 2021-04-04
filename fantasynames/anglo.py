from fantasynames.data import human_data
from fantasynames.language import Language
import random


class Anglo(Language):
    transformations = human_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        # 50% chance of just using one col (aka one syllable)
        if random.random() * 100 < 50:
            cols = [human_data["name1_col1"]]
        else:
            cols = [human_data["name1_col1"], human_data["name1_col2"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        name = cls._name1_male() + cls._name_from_lists([human_data["name1_suffixes"]])
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [human_data["name2_col1"], human_data["name2_col2"]]
        name = cls._name_from_lists(cols)
        # 50% chance to use "name1 of name2" format
        if random.random() * 100 < 50:
            return "of " + name
        else:
            return name


anglo = Anglo.name
