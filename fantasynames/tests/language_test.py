from fantasynames.gender import Gender
from fantasynames.languages.language import Language

# This file tests to make sure the basic process for name generation
# works as expected.

name1_col1 = ["lY"]
name1_col2 = ["n"]
name1_female_suffixes = ["a"]
name2_col1 = ["Ux"]
name2_col2 = ["tUn"]

test_transformations = [
    {"input": "Y", "outputs": ["e"]},
    {"input": "U", "outputs": ["o"]},
]


class TestLanguage(Language):
    transformations = test_transformations

    def first_name_male(self) -> str:
        cols = [name1_col1, name1_col2]
        return Language._name_from_lists(cols)

    def first_name_female(self) -> str:
        name = self.first_name_male() + Language._name_from_lists(
            [name1_female_suffixes]
        )
        return name

    def last_name(self) -> str:
        cols = [name2_col1, name2_col2]
        name = Language._name_from_lists(cols)
        return name


def test_name():
    name = TestLanguage().name()
    assert name == "Lena Oxton" or name == "Len Oxton"


def test_male_name():
    name = TestLanguage().name(Gender.MALE)
    assert name == "Len Oxton"


def test_female_name():
    name = TestLanguage().name(Gender.FEMALE)
    assert name == "Lena Oxton"
