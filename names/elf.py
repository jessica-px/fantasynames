from names.data import elf_data, compound_tables
from names.helpers import define_parse_string, gen_from_table
import random

# -----------------------------
#           Elf Names
# -----------------------------

parse_elf = define_parse_string(elf_data['patterns'])

def gen_elf_name1():
    name = gen_from_table(elf_data['name1_col1'], elf_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(elf_data['name1_suffixes'])

    return parse_elf(name).capitalize()

def gen_elf_name2():
    # 50% chance of using a nature name VS elfy name
    if random.random() * 100 < 50:
        name = gen_from_table(elf_data['name1_col1'], elf_data['name2_col2'])
    else:
        name = gen_from_table(compound_tables['nature_col1'], compound_tables['nature_col2'])

    return parse_elf(name).capitalize()

def generate_elf_name():
    return gen_elf_name1() + " " + gen_elf_name2()
