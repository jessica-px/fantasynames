from fantasynames.data import anglo_data, compound_tables
from fantasynames.language import Language
from fantasynames.anglo import Anglo
from fantasynames.french import French
import random


class Human(Language):
    @classmethod
    def _name1_male(cls) -> str:
        # 80% chance anglo name, 20% chance french
        if random.random() * 100 <= 20:
            name = French._name1("male")
        else:
            name = Anglo._name1("male")
        return name

    @classmethod
    def _name1_female(cls) -> str:
        # 80% chance anglo name, 20% chance french
        if random.random() * 100 <= 20:
            name = French._name1("female")
        else:
            name = Anglo._name1("female")
        return name

    @classmethod
    def _name2(cls) -> str:
        prob = random.random() * 100
        # 25% chance of anglo surname
        if prob <= 25:
            name = Anglo._name2()
        # 25% chance of french surname
        elif prob <= 50:
            name = French._name2()
        # 50% chance surname is cobbled together from various tables
        else:
            col1 = random.choice(
                [
                    compound_tables["mountain_col1"],
                    compound_tables["nature_col1"],
                    compound_tables["generic_col1"],
                    compound_tables["generic_col1"],
                ]
            )
            col2 = random.choice(
                [
                    compound_tables["mountain_col2"],
                    compound_tables["nature_col2"],
                    compound_tables["generic_col2"],
                    compound_tables["generic_col2"],
                    anglo_data["name2_col2"],
                ]
            )
            name = cls._name_from_lists([col1, col2])

        return name


human = Human.name
