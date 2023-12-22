import random

from fantasynames.data import dwarf_data, compound_tables
from fantasynames.languages.language import Language


class Dwarf(Language):
    transformations = dwarf_data["transformations"]

    def first_name_male(self) -> str:
        cols = [dwarf_data["name1_col1"], dwarf_data["name1_col2"]]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
        # 50% to add "-a" to a male name
        if random.random() * 100 < 50:
            return f"{self.first_name_male()}a"
        # 50% chance to use female col for second half of name
        else:
            cols = [dwarf_data["name1_col1"], dwarf_data["name1_col2_female"]]
            name = Language._name_from_lists(cols)
        return name

    def last_name(self) -> str:
        cols = [compound_tables["mountain_col1"], compound_tables["mountain_col2"]]
        name = Language._name_from_lists(cols)
        return name
