from fantasynames.data import french_data
import random
from fantasynames.language import Language


class French(Language):
    transformations = french_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        # 50% chance col1 + col2
        if random.random() * 100 <= 50:
            cols = [french_data["name1_col1"], french_data["name1_col2"]]
        # 50% chance col1 + male suffix
        else:
            cols = [french_data["name1_col1"], french_data["name1_male_suffixes"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        name = cls._name_from_lists(
            [
                french_data["name1_col1"],
                french_data["name1_col2"],
                french_data["name1_female_suffixes"],
            ]
        )
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [french_data["name2_col1"], french_data["name2_col2"]]
        name = cls._name_from_lists(cols)
        # 50% chance to use "name1 d' name2" or "name1 du name2" format
        if random.random() * 100 <= 30:
            prefix = random.choice(french_data["name2_prefixes"])
            name = prefix + name
        return name


french = French.name
