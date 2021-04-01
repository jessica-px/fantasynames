from names.data import hobbit_data, elf_data, dwarf_data, human_data, french_data, compound_tables
from names.helpers import define_generate_language, define_parse_string, gen_from_table
from names.french import generate_french_name1, generate_french_name2
from names.anglo import generate_anglo_name1, generate_anglo_name2
import random

# -----------------------------
#           Human Mishmash Names
# -----------------------------

def gen_mishmash_name1():
    # 50% chance of English/French
    if random.random() * 100 <= 50:
        name = generate_french_name1()
    else:
        name = generate_anglo_name1()
    return name

def gen_mishmash_name2():
    prob = random.random() * 100
    # 20% chance of english surname
    if prob <= 20:
        name = generate_anglo_name2()
    # 20% chance of french surname
    elif prob <= 40:
        name = generate_french_name2()
    # 60% chance surname is cobbled together from various tables
    else:
        col1 = random.choice([
            compound_tables['mountain_col1'],
            compound_tables['nature_col1'],
            compound_tables['generic_col1'],
            compound_tables['generic_col1']
        ])
        col2 = random.choice([
            compound_tables['mountain_col2'],
            compound_tables['nature_col2'],
            compound_tables['generic_col2'],
            compound_tables['generic_col2'],
            human_data['name2_col2']
        ])
        name = gen_from_table(col1, col2)

    return name

def generate_human_name():
    gen_mishmash_name1() + " " + gen_mishmash_name2()
