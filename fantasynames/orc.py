from fantasynames.language import Language
from fantasynames.data import orc_data

class Orc(Language):

    @classmethod
    def _name1_any(cls) -> str:
        return cls._name_from_lists([orc_data["name1_col1"], orc_data["name1_col2"]])

    # @classmethod
    # def _name1_female(cls) -> str:
    #     return cls._name1_male()

orc = Orc.name