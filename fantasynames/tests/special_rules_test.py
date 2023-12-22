from fantasynames.gender import Gender
from fantasynames.languages.language import Language


# This file test to make sure capitalization and special transformation
# rules are applied as expected.


class TestLanguage(Language):
    def first_name_male(self) -> str:
        return "bob*y"

    def first_name_female(self) -> str:
        return "jack*y"

    def last_name(self) -> str:
        return "the brave d'blanche"


def test_male_name():
    name = TestLanguage().name(Gender.MALE)
    assert name == "Bobby the Brave d'Blanche"


def test_female_name():
    name = TestLanguage().name(Gender.FEMALE)
    assert name == "Jacky the Brave d'Blanche"


def test_ampersand():
    name = "dun" + "r&ic"
    transformed_name = TestLanguage()._transform(name)
    assert transformed_name == "dunic"


def test_ampersand_2():
    name = "e" + "r&ic"
    transformed_name = TestLanguage()._transform(name)
    assert transformed_name == "eric"


def test_pound():
    name = "and" + "r#e"
    transformed_name = TestLanguage()._transform(name)
    assert transformed_name == "andre"


def test_pound_2():
    name = "ann" + "r#e"
    transformed_name = TestLanguage()._transform(name)
    assert transformed_name == "anne"
