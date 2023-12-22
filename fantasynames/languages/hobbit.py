from fantasynames.data import hobbit_data
from fantasynames.languages.language import Language


class Hobbit(Language):
    transformations = hobbit_data["transformations"]

    def first_name_male(self) -> str:
        cols = [hobbit_data["name1_col1"], hobbit_data["name1_male_suffixes"]]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
        cols = [hobbit_data["name1_col1"], hobbit_data["name1_female_suffixes"]]
        return Language._name_from_lists(cols)

    def last_name(self) -> str:
        cols = [hobbit_data["name2_col1"], hobbit_data["name2_col2"]]
        name = Language._name_from_lists(cols)
        return name
