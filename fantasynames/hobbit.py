from fantasynames.data import hobbit_data
from fantasynames.language import Language


class Hobbit(Language):
    transformations = hobbit_data["transformations"]

    @classmethod
    def _name1_male(cls) -> str:
        cols = [hobbit_data["name1_col1"], hobbit_data["name1_male_suffixes"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        cols = [hobbit_data["name1_col1"], hobbit_data["name1_female_suffixes"]]
        return cls._name_from_lists(cols)

    @classmethod
    def _name2(cls) -> str:
        cols = [hobbit_data["name2_col1"], hobbit_data["name2_col2"]]
        name = cls._name_from_lists(cols)
        return name


hobbit = Hobbit.name
