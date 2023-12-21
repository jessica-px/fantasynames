import random

from fantasynames.dwarf import Dwarf
from fantasynames.elf import Elf
from fantasynames.hobbit import Hobbit
from fantasynames.human_diverse import Human
from fantasynames.language import Language

_LANGUAGES = [Dwarf, Elf, Hobbit, Human]


class RandomLanguage(Language):
    @classmethod
    def _get_random_language(cls) -> type[Language]:
        return random.choice(_LANGUAGES)

    @classmethod
    def _name1_male(cls) -> str:
        return RandomLanguage._get_random_language()._name1("male")

    @classmethod
    def _name1_female(cls) -> str:
        return RandomLanguage._get_random_language()._name1("female")

    @classmethod
    def _name2(cls) -> str:
        return RandomLanguage._get_random_language()._name2()


random_language = RandomLanguage.name
