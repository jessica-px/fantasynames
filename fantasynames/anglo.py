from fantasynames.data import anglo_data
from fantasynames.language import Language
import random


class Anglo(Language):
    transformations = anglo_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        prob = random.random() * 100
        # 50% chance to use col1 + col2
        if prob < 50:
            cols = [anglo_data["name1_col1"], anglo_data["name1_col2"]]
        # 50% chance to use col1 + a male suffix
        else:
            cols = [anglo_data["name1_col1"], anglo_data["name1_male_suffixes"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        prob = random.random() * 100
        # 50% chance of just using col1 + female suffix
        if prob < 50:
            cols = [anglo_data["name1_col1"], anglo_data["name1_female_suffixes"]]
        # 50% chance of col1 + col2 + female suffix
        else:
            cols = [
                anglo_data["name1_col1"],
                anglo_data["name1_col2"],
                anglo_data["name1_female_suffixes"],
            ]
        return cls._name_from_lists(cols)

    @classmethod
    def _name2(cls) -> str:
        cols = [anglo_data["name2_col1"], anglo_data["name2_col2"]]
        name = cls._name_from_lists(cols)
        # 50% chance to use "name1 of name2" format
        if random.random() * 100 < 50:
            return "of " + name
        else:
            return name


anglo = Anglo.name
