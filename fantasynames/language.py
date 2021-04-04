from abc import ABC, abstractmethod
import typing as t
import random


class Language(ABC):
    transformations: t.List[t.Dict]

    @classmethod
    def name(cls, gender: str = "any") -> str:
        """
        Returns a randomly generated first and last name. This is the only method
        that we intend to be "publicly" used outside of this class.
        """
        return cls._name1(gender) + " " + cls._name2()

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

        return cls._transform(name)

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
            - *: repeat the previous character
        """
        new_string = ""
        for char in name:
            new_char = char
            for transformation in cls.transformations:
                if char == transformation["input"]:
                    new_char = random.choice(transformation["outputs"])
                    break
                if char == "*":
                    new_char = new_string[-1]
            new_string += new_char
        return new_string.capitalize()

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