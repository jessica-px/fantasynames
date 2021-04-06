from fantasynames.language import Language

# This file tests to make sure the basic process for name generation
# works as expected.

name1_col1 = ["lY"]
name1_col2 = ["n"]
name1_female_suffixes = ["a"]
name2_col1 = ["Ux"]
name2_col2 = ["tUn"]

test_tranformations = [
    {"input": "Y", "outputs": ["e"]},
    {"input": "U", "outputs": ["o"]},
]


class TestLanguage(Language):
    transformations = test_tranformations

    @classmethod
    def _name1_male(cls) -> str:
        cols = [name1_col1, name1_col2]
        return cls._name_from_lists(cols)

    @classmethod
    def _name1_female(cls) -> str:
        name = cls._name1_male() + cls._name_from_lists([name1_female_suffixes])
        return name

    @classmethod
    def _name2(cls) -> str:
        cols = [name2_col1, name2_col2]
        name = cls._name_from_lists(cols)
        return name


def test_name():
    name = TestLanguage.name()
    assert name == "Lena Oxton" or name == "Len Oxton"


def test_male_name():
    name = TestLanguage.name("male")
    assert name == "Len Oxton"


def test_female_name():
    name = TestLanguage.name("female")
    assert name == "Lena Oxton"
