from fantasynames.data import dwarf_data, compound_tables
from fantasynames.language import Language
import random


class Dwarf(Language):
    transformations = dwarf_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        cols = [dwarf_data["name1_col1"], dwarf_data["name1_col2"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        # 50% to add "-a" to a male name
        if random.random() * 100 < 50:
            name = cls._name1_male() + "a"
        # 50% chance to use female col for second half of name
        else:
            cols = [dwarf_data["name1_col1"], dwarf_data["name1_col2_female"]]
            name = cls._name_from_lists(cols)
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [compound_tables["mountain_col1"], compound_tables["mountain_col2"]]
        name = cls._name_from_lists(cols)
        return name


dwarf = Dwarf.name
