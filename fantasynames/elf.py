from fantasynames.data import elf_data, compound_tables
from fantasynames.language import Language
import random


class Elf(Language):
    transformations = elf_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        cols = [elf_data["name1_col1"], elf_data["name1_col2"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        name = cls._name1_male() + cls._name_from_lists(
            [elf_data["name1_female_suffixes"]]
        )
        return name

    @classmethod
    def _name2(cls) -> str:
        # 50% chance of elf-y surname or nature-y surname
        if random.random() * 100 < 50:
            cols = [compound_tables["nature_col1"], compound_tables["nature_col2"]]
        else:
            cols = [elf_data["name1_col1"], elf_data["name2_col2"]]

        name = cls._name_from_lists(cols)
        return name


elf = Elf.name
