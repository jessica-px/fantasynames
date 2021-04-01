from names.data import human_data
from names.helpers import define_generate_language, define_parse_string, gen_from_table
import random

# -----------------------------
#           Anglo Names
# -----------------------------
parse_anglo = define_parse_string(human_data['patterns'])

def generate_anglo_name1():
    # 50% chance of only using col1
    if random.random() * 100 < 50:
        name = random.choice(human_data['name1_col1'])
    else:
        name = gen_from_table(human_data['name1_col1'], human_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(human_data['name1_suffixes'])
    return name

def generate_anglo_name2():
    name = gen_from_table(human_data['name2_col1'], human_data['name2_col2'])
    # also, 50% chance to use "name1 of name2" format
    if random.random() * 100 <= 50:
        name = 'of ' + name
    return name

generate_anglo_name = define_generate_language(parse_anglo, generate_anglo_name1, generate_anglo_name2)
