import random
from abc import ABC, abstractmethod
from typing import Callable

from fantasynames.gender import Gender

NOT_TO_UPPERCASE = ["of", "du", "del", "de", "la", "von", "the"]


class Language(ABC):
    transformations: list[dict] = []

    def __init__(self):
        self.gender_to_first_name_method: dict[Gender, Callable[[], str]] = {
            Gender.MALE: self.first_name_male,
            Gender.FEMALE: self.first_name_female,
            Gender.ANY: self.first_name_any,
        }

    def __call__(self, gender: Gender = Gender.ANY):
        return self.name(gender)

    def name(self, gender: Gender = Gender.ANY) -> str:
        """
        Returns a randomly generated first and last name. This is the only method
        that we intend to be "publicly" used outside of this package.
        """
        name = f"{self.first_name(gender)} {self.last_name()}"
        transformed_name = self._transform(name)
        caps_name = Language._capitalize(transformed_name)
        return caps_name

    def first_name(self, gender: Gender = Gender.ANY) -> str:
        """
        Returns a randomly generated first name with variable gender.
        By default, randomly chooses either masculine or feminine.
        """
        name_generator = self.gender_to_first_name_method[gender]
        return name_generator()

    @abstractmethod
    def first_name_female(self) -> str:
        """
        Expected to return a random 'feminine' first name. Must be overridden.
        """
        pass

    @abstractmethod
    def first_name_male(self) -> str:
        """
        Expected to return a random 'masculine' first name. Must be overridden.
        """
        pass

    def first_name_any(self) -> str:
        """
        Randomly returns either a masculine or feminine first name (50/50 chance).
        """
        return random.choice([self.first_name_male(), self.first_name_female()])

    @abstractmethod
    def last_name(self) -> str:
        """
        Expected to return a random surname. Must be overridden.
        """
        pass

    def _transform(self, name: str) -> str:
        """
        Given a string, loops over each char. If 'input' is present in the
        `cls.transformations` dict, "replaces" it with a randomly
        selected character from the dict. Returns a new string with the newly
        replaced chars. (No actual mutations performed.)

        Also has the following special rules for special "input" characters:
            - *: doubles previous char if not preceded by a CVC pattern
        """
        new_string = ""
        for char in name:
            new_char = char
            prev_char = new_string[-1] if len(new_string) > 0 else ""
            prev_prev_char = new_string[-2] if len(new_string) > 1 else ""

            # "*" doubles previous char if not preceded by a CVC pattern
            # Ex: 'wil' + '*and' -> "willand", "wald" + '*and' -> 'waldan'
            if char == "*":
                if _double_consonant(new_string):
                    new_char = prev_char
                else:
                    new_char = ""
            # "&" removes preceeding char if it's preceeded by a consontant
            # Ex: 'ia' + 'l&er' -> 'ialer', 'sand' + 'l&er' -> 'sander'
            if char == "&":
                if _is_vowel(prev_prev_char):
                    new_char = ""
                else:
                    new_string = new_string[:-1]
                    new_char = ""
            # "#" removes preceding char unless it's preceded by a plosive
            # Ex: 'and' + 'r#e' -> 'andre', 'sir' + 'r#e' -> 'sire'
            if char == "#":
                if prev_prev_char in "pbdtkgc":
                    new_char = ""
                else:
                    new_string = new_string[:-1]
                    new_char = ""
            # checks is character is in given transformations
            for transformation in self.transformations:
                if char == transformation["input"]:
                    new_char = random.choice(transformation["outputs"])
                    break
            new_string += new_char
        return new_string

    @classmethod
    def _capitalize(cls, name: str) -> str:
        caps_list = []
        for word in name.split():
            # leave particles lowercase
            if word in NOT_TO_UPPERCASE:
                caps_list.append(word)
            # handle d'
            elif word[:2] == "d'":
                fragment = word[2:].capitalize()
                caps_list.append("d'" + fragment)
            # capitalize the rest
            else:
                caps_list.append(word.capitalize())
        return " ".join(caps_list)

    @classmethod
    def _name_from_lists(cls, lists: list[list[str]]) -> str:
        """
        Given one or more list of strings, randomly selects a string from each
        and returns the concatenated result.
        """
        name = ""
        for string_list in lists:
            name += random.choice(string_list)
        return name


# ----------------------
#        Helpers
# ----------------------


def _is_vowel(char: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    return char in vowels


def _double_consonant(string: str) -> bool:
    """
    The "double consonant rule" means that if the chars preceding a special character
    ("*" in our case) match a consonant-vowel-consonant pattern, we double the
    final consonant. This helper function tests for that pattern.
    Examples if true: bob*y -> bobby, rin*e -> rinne
    Examples if false: rick*y -> ricky, wood*y -> woody
    """
    if len(string) < 3:
        return True

    prev_chars = string[-3:]
    pattern = ""
    for char in prev_chars:
        if _is_vowel(char):
            pattern += "V"
        else:
            pattern += "C"
    return pattern == "CVC"
