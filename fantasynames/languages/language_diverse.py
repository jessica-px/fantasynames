from typing import Optional

from numpy.random import choice

from fantasynames.consts import DEFAULT_RANDOM_LANGUAGES
from fantasynames.gender import Gender
from fantasynames.languages.language import Language


class LanguageDiverse(Language):
    def __init__(
        self,
        languages: list[Language] = DEFAULT_RANDOM_LANGUAGES,
        first_name_prob: Optional[list[float]] = None,
        last_name_prob: Optional[list[float]] = None,
    ):
        super().__init__()
        self.languages = languages
        self.first_name_prob = (
            first_name_prob
            if first_name_prob
            else [1 / len(languages) for _ in range(len(languages))]
        )
        self.last_name_prob = (
            last_name_prob
            if last_name_prob
            else [1 / len(languages) for _ in range(len(languages))]
        )

    def get_rand_lang(self, is_first_name: bool) -> Language:
        prob = self.first_name_prob if is_first_name else self.last_name_prob
        return choice(self.languages, p=prob)

    def first_name_male(self) -> str:
        return self.get_rand_lang(is_first_name=True).first_name(Gender.MALE)

    def first_name_female(self) -> str:
        return self.get_rand_lang(is_first_name=True).first_name(Gender.FEMALE)

    def last_name(self) -> str:
        return self.get_rand_lang(is_first_name=False).last_name()
