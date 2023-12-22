import random

from numpy.random import choice

from fantasynames.data import french_data
from fantasynames.languages.language import Language


class French(Language):
    transformations = french_data["transformations"]

    def first_name_male(self) -> str:
        # 50% chance col1 + col2
        if random.random() * 100 <= 50:
            cols = [french_data["name1_col1"], french_data["name1_col2"]]
        # 50% chance col1 + male suffix
        else:
            cols = [french_data["name1_col1"], french_data["name1_male_suffixes"]]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
        name = Language._name_from_lists(
            [
                french_data["name1_col1"],
                french_data["name1_col2"],
                french_data["name1_female_suffixes"],
            ]
        )
        return name

    def last_name(self) -> str:
        """
        50% chance to use "name1 d' name2" or "name1 du name2" format
        """
        cols = [french_data["name2_col1"], french_data["name2_col2"]]
        name = Language._name_from_lists(cols)
        optional_prefix = random.choice(french_data["name2_prefixes"])
        return choice([name, f"{optional_prefix}{name}"], p=[0.7, 0.3])
