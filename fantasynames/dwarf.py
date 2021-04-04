from fantasynames.data import dwarf_data, compound_tables
from fantasynames.language import Language


class Dwarf(Language):
    transformations = dwarf_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        cols = [dwarf_data["name1_col1"], dwarf_data["name1_col2"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        name = cls._name1_male() + cls._name_from_lists([dwarf_data["name1_suffixes"]])
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [compound_tables["mountain_col1"], compound_tables["mountain_col2"]]
        name = cls._name_from_lists(cols)
        return name


dwarf = Dwarf.name
