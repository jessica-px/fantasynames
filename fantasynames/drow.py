from fantasynames.data import drow_data
from fantasynames.language import Language
import random


class Drow(Language):
    @classmethod
    def _name1_male(cls) -> str:
        cols = [drow_data["name1_col1_male"], drow_data["name1_col2_male"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        cols = [drow_data["name1_col1_female"], drow_data["name1_col2_female"]]
        name = cls._name_from_lists(cols)
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [drow_data["name2_col1"], drow_data["name2_col2"]]
        name = cls._name_from_lists(cols)
        return name


drow = Drow.name
