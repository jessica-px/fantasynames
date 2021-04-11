from abc import ABC, abstractmethod
import typing as t
import random


class Language(ABC):
    transformations: t.List[t.Dict] = []

    @classmethod
    def name(cls, gender: str = "any") -> str:
        """
        Returns a randomly generated first and last name. This is the only method
        that we intend to be "publicly" used outside of this package.
        """
        name = cls._name1(gender) + " " + cls._name2()
        transformed_name = cls._transform(name)
        caps_name = cls._capitalize(transformed_name)
        return caps_name

    @classmethod
    def _name1(cls, gender: str = "any") -> str:
        """
        Returns a randomly generated first name with variable gender.
        By default, randomly chooses either masculine or feminine.
        """
        if gender == "female":
            name = cls._name1_female()
        elif gender == "male":
            name = cls._name1_male()
        elif gender == "any":
            name = cls._name1_any()
        else:
            msg = (
                "Valid string parameters for name generating functions are "
                '"female", "male", or "any". The given value was the '
                f'{type(gender).__name__} "{gender}".'
            )
            raise ValueError(msg)

        return name

    @classmethod
    @abstractmethod
    def _name1_female(cls) -> str:
        """
        Expected to return a random 'feminine' first name. Must be overridden.
        """
        pass

    @classmethod
    @abstractmethod
    def _name1_male(cls) -> str:
        """
        Expected to return a random 'masculine' first name. Must be overridden.
        """
        pass

    @classmethod
    def _name1_any(cls) -> str:
        """
        Randomly returns either a masculine or feminine first name (50/50 chance).
        """
        if random.random() * 100 < 50:
            return cls._name1_male()
        else:
            return cls._name1_female()

    @classmethod
    @abstractmethod
    def _name2(cls) -> str:
        """
        Expected to return a random surname. Must be overridden.
        """
        pass

    @classmethod
    def _transform(cls, name: str) -> str:
        """
        Given a string, loops over each char. If 'input' is present in the
        cls.transformations dict, "replaces" it with a randomly
        selected character from the dict. Returns a new string with the newly
        replaced chars. (No actual mutations performed.)

        Also has the following special rules for special "input" characters:
            - *: doubles previous char if not preceeded by a CVC pattern
        """
        new_string = ""
        for char in name:
            new_char = char
            prev_char = new_string[-1] if len(new_string) > 0 else ""
            prev_prev_char = new_string[-2] if len(new_string) > 1 else ""

            # "*" doubles previous char if not preceeded by a CVC pattern
            # Ex: 'wil' + '*and' -> "willand", "wald" + '*and' -> 'waldan'
            if char == "*":
                if double_consonant(new_string):
                    new_char = prev_char
                else:
                    new_char = ""
            # "&" removes preceeding char if it's preceeded by a consontant
            # Ex: 'ia' + 'l&er' -> 'ialer', 'sand' + 'l&er' -> 'sander'
            if char == "&":
                if is_vowel(prev_prev_char):
                    new_char = ""
                else:
                    new_string = new_string[:-1]
                    new_char = ""
            # "#" removes preceeding char unless it's preceeded by a plosive
            # Ex: 'and' + 'r#e' -> 'andre', 'sir' + 'r#e' -> 'sire'
            if char == "#":
                if prev_prev_char in "pbdtkgc":
                    new_char = ""
                else:
                    new_string = new_string[:-1]
                    new_char = ""
            # checks is character is in given transformations
            for transformation in cls.transformations:
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
            if word in ["of", "du", "del", "de", "la", "von", "the"]:
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
    def _name_from_lists(cls, lists: t.List[t.List[str]]) -> str:
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


def is_vowel(char: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    return char in vowels


def double_consonant(string: str) -> bool:
    # the "double consonat rule" means that if the chars preceeding a special character
    # ("*" in our case) match a consonant-vowel-consonant pattern, we double the
    # final consonant. This helper function tests for that pattern.
    # Examples if true: bob*y -> bobby, rin*e -> rinne
    # Examples if false: rick*y -> ricky, wood*y -> woody
    if len(string) < 3:
        return True

    prev_chars = string[-3:]
    pattern = ""
    for char in prev_chars:
        if is_vowel(char):
            pattern += "V"
        else:
            pattern += "C"
    return pattern == "CVC"
