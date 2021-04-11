from fantasynames.language import Language

# This file test to make sure capitalization and special transformation
# rules are applied as expected.


class TestLanguage(Language):
    @classmethod
    def _name1_male(cls) -> str:
        return "bob*y"

    @classmethod
    def _name1_female(cls) -> str:
        return "jack*y"

    @classmethod
    def _name2(cls) -> str:
        return "the brave d'blanche"


def test_male_name():
    name = TestLanguage.name("male")
    assert name == "Bobby the Brave d'Blanche"


def test_female_name():
    name = TestLanguage.name("female")
    assert name == "Jacky the Brave d'Blanche"


def test_ampersand():
    name = "dun" + "r&ic"
    transformed_name = TestLanguage._transform(name)
    assert transformed_name == "dunic"


def test_ampersand_2():
    name = "e" + "r&ic"
    transformed_name = TestLanguage._transform(name)
    assert transformed_name == "eric"


def test_pound():
    name = "and" + "r#e"
    transformed_name = TestLanguage._transform(name)
    assert transformed_name == "andre"


def test_pound_2():
    name = "ann" + "r#e"
    transformed_name = TestLanguage._transform(name)
    assert transformed_name == "anne"
