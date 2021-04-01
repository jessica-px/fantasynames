from names.data import dwarf_data, compound_tables
from names.helpers import define_parse_string, gen_from_table
import random

# -----------------------------
#           Dwarf Names
# -----------------------------

parse_dwarf = define_parse_string(dwarf_data['patterns'])

def gen_dwarf_name1():
    name = gen_from_table(dwarf_data['name1_col1'], dwarf_data['name1_col2'])
    # 30% chance of adding a suffix
    if random.random() * 100 < 30:
        name += random.choice(dwarf_data['name1_suffixes'])
    return parse_dwarf(name).capitalize()

def gen_dwarf_name2():
    name = gen_from_table(compound_tables['mountain_col1'], compound_tables['mountain_col2'])
    return name.capitalize()

def generate_dwarf_name():
    return gen_dwarf_name1() + " " + gen_dwarf_name2()
