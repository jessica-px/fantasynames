import random

from fantasynames.data import anglo_data
from fantasynames.languages.language import Language


class Anglo(Language):
    transformations = anglo_data["transformations"]

    def first_name_male(self) -> str:
        prob = random.random() * 100
        # 50% chance to use col1 + col2
        if prob < 50:
            cols = [anglo_data["name1_col1"], anglo_data["name1_col2"]]
        # 50% chance to use col1 + a male suffix
        else:
            cols = [anglo_data["name1_col1"], anglo_data["name1_male_suffixes"]]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
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
        return Language._name_from_lists(cols)

    def last_name(self) -> str:
        """
        50% chance to use "name1 of name2" format
        """
        cols = [anglo_data["name2_col1"], anglo_data["name2_col2"]]
        name = Language._name_from_lists(cols)
        return random.choice([f"of {name}", name])
