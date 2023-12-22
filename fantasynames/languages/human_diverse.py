import random

from fantasynames.consts import DEFAULT_HUMAN_LANGUAGES
from fantasynames.data import anglo_data, compound_tables
from fantasynames.languages.language import Language
from fantasynames.languages.language_diverse import LanguageDiverse


class Human(LanguageDiverse):
    def __init__(self):
        super().__init__(languages=DEFAULT_HUMAN_LANGUAGES, first_name_prob=[0.2, 0.8])

        self.last_name_col1 = [
            compound_tables["mountain_col1"],
            compound_tables["nature_col1"],
            compound_tables["generic_col1"],
            compound_tables["generic_col1"],
        ]

        self.last_name_col2 = [
            compound_tables["mountain_col2"],
            compound_tables["nature_col2"],
            compound_tables["generic_col2"],
            compound_tables["generic_col2"],
            anglo_data["name2_col2"],
        ]

    def last_name(self) -> str:
        """
        25% chance of anglo surname
        25% chance of french surname
        50% chance surname is cobbled together from various tables
        """
        name = self.get_rand_lang(is_first_name=False).last_name()
        if random.random() < 0.5:
            return name

        col1 = random.choice(self.last_name_col1)
        col2 = random.choice(self.last_name_col2)

        name = Language._name_from_lists([col1, col2])

        return name
