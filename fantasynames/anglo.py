from fantasynames.data import human_data
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Helpers
# -----------------------------

transform_anglo = define_transform_function(human_data["transformations"])


def generate_anglo_name1_base() -> str:
    """
    Outputs a randomized (masculine) "Anglo" first name.
    """
    # 50% chance of only using col1
    if random.random() * 100 < 50:
        name = random.choice(human_data["name1_col1"])
    else:
        name = gen_from_table(human_data["name1_col1"], human_data["name1_col2"])
    return transform_anglo(name).capitalize()


def generate_anglo_name1_female() -> str:
    """
    Outputs a randomized "Anglo" first name with a feminine suffix.
    """
    name = generate_anglo_name1_base() + random.choice(human_data["name1_suffixes"])
    return transform_anglo(name).capitalize()


def generate_anglo_name1(gender: str = "any") -> str:
    """
    Outputs a randomized "Anglo" first name with variable gender.
    """
    if gender == "female":
        return generate_anglo_name1_female()
    elif gender == "male":
        return generate_anglo_name1_base()
    elif gender == "any":  # 50% chance of male or female first name
        if random.random() * 100 < 50:
            return generate_anglo_name1_base()
        else:
            return generate_anglo_name1_female()
    else:
        raise ValueError(
            f'Valid string parameters for name generating functions are "female", "male", or "any". The given value was the {type(gender).__name__} "{gender}".'
        )


def generate_anglo_name2() -> str:
    """
    Outputs a randomized "Anglo" surname.
    """
    # 50% chance to use "name1 of name2" format
    if random.random() * 100 <= 50:
        name = gen_from_table(human_data["name2_col1"], human_data["name2_col2"])
        name = transform_anglo(name).capitalize()
        return "of " + name
    else:
        name = gen_from_table(human_data["name2_col1"], human_data["name2_col2"])
        return transform_anglo(name).capitalize()


# -----------------------------
#   Name Generating Function
# -----------------------------


def generate_anglo_name(gender: str = "any") -> str:
    """
    Outputs a randomized "Anglo" first and last name, with the first name having
    variable gender.
    """
    return generate_anglo_name1(gender) + " " + generate_anglo_name2()
