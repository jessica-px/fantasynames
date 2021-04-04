from fantasynames.data import dwarf_data, compound_tables
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Helpers
# -----------------------------

transform_dwarf = define_transform_function(dwarf_data["transformations"])


def gen_dwarf_name1_base() -> str:
    """
    Outputs a randomized (masculine) "dwarf" first name.
    """
    name = gen_from_table(dwarf_data["name1_col1"], dwarf_data["name1_col2"])
    return name


def generate_dwarf_name1_female() -> str:
    """
    Outputs a randomized "dwarf" first name with a feminine suffix.
    """
    name = gen_dwarf_name1_base() + random.choice(dwarf_data["name1_suffixes"])
    return name


def gen_dwarf_name1(gender: str) -> str:
    """
    Outputs a randomized "dwarf" first name with variable gender.
    """
    if gender == "female":
        name = generate_dwarf_name1_female()
    elif gender == "male":
        name = gen_dwarf_name1_base()
    elif gender == "any":  # 50% chance of male or female first name
        if random.random() * 100 < 50:
            name = gen_dwarf_name1_base()
        else:
            name = generate_dwarf_name1_female()
    else:
        raise ValueError(
            f'Valid string parameters for name generating functions are "female", "male", or "any". The given value was the {type(gender).__name__} "{gender}".'
        )
    return transform_dwarf(name).capitalize()


def gen_dwarf_name2() -> str:
    """
    Outputs a randomized "dwarf" surname.
    """
    name = gen_from_table(
        compound_tables["mountain_col1"], compound_tables["mountain_col2"]
    )
    return name.capitalize()


# -----------------------------
#   Name Generating Function
# -----------------------------


def generate_dwarf_name(gender: str = "any") -> str:
    """
    Outputs a randomized "dwarf" first and last name, with the first name having
    variable gender.
    """
    return gen_dwarf_name1(gender) + " " + gen_dwarf_name2()
