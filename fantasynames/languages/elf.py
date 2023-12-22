import random

from fantasynames.data import elf_data, compound_tables
from fantasynames.languages.language import Language


class Elf(Language):
    transformations = elf_data["transformations"]

    def first_name_male(self) -> str:
        cols = [elf_data["name1_col1"], elf_data["name1_col2"]]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
        name = self.first_name_male() + Language._name_from_lists(
            [elf_data["name1_female_suffixes"]]
        )
        return name

    def last_name(self) -> str:
        """
        50% chance of elf-y surname or nature-y surname
        """
        cols = random.choice(
            [
                [compound_tables["nature_col1"], compound_tables["nature_col2"]],
                [elf_data["name1_col1"], elf_data["name2_col2"]],
            ]
        )
        name = Language._name_from_lists(cols)
        return name
