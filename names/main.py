from names.data import hobbit_data, elf_data, dwarf_data, human_data, french_data, compound_tables
from names.helpers import define_generate_language, define_parse_string, gen_from_table
import random

'''
In this file, we write the logic that generates the various fantasy names.
String data is expected to be imported from data.py, while repeatable logic
should be imported as helper functions from helpers.py whenever possible.

For a given name generator, we expect one master function to be defined,
with the naming scheme `generate_foo_name()`. This function should, whenever
possible, be made with the the HOF `define_generate_language()` for consistency.

Make sure to add your function to __init__.py when done, for accessibility.
'''

# -----------------------------
#           Hobbit Names
# -----------------------------

parse_hobbit = define_parse_string(hobbit_data['patterns'])

def gen_hobbit_name1():
    return gen_from_table(hobbit_data['name1_col1'], hobbit_data['name1_col2'])
def gen_hobbit_name2():
    return gen_from_table(hobbit_data['name2_col1'], hobbit_data['name2_col2'])

generate_hobbit_name = define_generate_language(parse_hobbit, gen_hobbit_name1, gen_hobbit_name2)

# -----------------------------
#           Elf Names
# -----------------------------

parse_elf = define_parse_string(elf_data['patterns'])

def gen_elf_name1():
    name = gen_from_table(elf_data['name1_col1'], elf_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(elf_data['name1_suffixes'])

    return name

def gen_elf_name2():
    # 50% chance of using a nature name VS elfy name
    if random.random() * 100 < 50:
        name = gen_from_table(elf_data['name1_col1'], elf_data['name2_col2'])
    else:
        name = gen_from_table(compound_tables['nature_col1'], compound_tables['nature_col2'])

    return name

generate_elf_name = define_generate_language(parse_elf, gen_elf_name1, gen_elf_name2)

# -----------------------------
#           Dwarf Names
# -----------------------------

parse_dwarf = define_parse_string(dwarf_data['patterns'])

def gen_dwarf_name1():
    name = gen_from_table(dwarf_data['name1_col1'], dwarf_data['name1_col2'])
    # 30% chance of adding a suffix
    if random.random() * 100 < 30:
        name += random.choice(dwarf_data['name1_suffixes'])
    return name

def gen_dwarf_name2():
    return gen_from_table(compound_tables['mountain_col1'], compound_tables['mountain_col2'])

generate_dwarf_name = define_generate_language(parse_dwarf, gen_dwarf_name1, gen_dwarf_name2)

# -----------------------------
#           French Names
# -----------------------------
parse_french = define_parse_string(french_data['patterns'])

def generate_french_name1():
    return gen_from_table(french_data['name1_col1'], french_data['name1_col2'])

def generate_french_name2():
    name = gen_from_table(french_data['name2_col1'], french_data['name2_col2'])
    # 30% chance of d' prefix
    if random.random() * 100 <= 30:
        prefix = random.choice(french_data['name2_prefixes'])
        name = prefix + name
    return name

generate_french_name = define_generate_language(parse_french, generate_french_name1, generate_french_name2)

# -----------------------------
#           English Names
# -----------------------------
parse_english = define_parse_string(human_data['patterns'])

def generate_english_name1():
    # 50% chance of only using col1
    if random.random() * 100 < 50:
        name = random.choice(human_data['name1_col1'])
    else:
        name = gen_from_table(human_data['name1_col1'], human_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(human_data['name1_suffixes'])
    return name

def generate_english_name2():
    name = gen_from_table(human_data['name2_col1'], human_data['name2_col2'])
    # also, 50% chance to use "name1 of name2" format
    if random.random() * 100 <= 50:
        name = 'of ' + name
    return name

generate_english_name = define_generate_language(parse_english, generate_english_name1, generate_english_name2)


# -------- Human nonsense below this line ------------------

# -----------------------------
#           Human Mishmash Names
# -----------------------------

def gen_mishmash_name1():
    # 50% chance of English/French
    if random.random() * 100 <= 50:
        name = parse_french(generate_french_name1())
    else:
        name = parse_english(generate_english_name1())
    return name

def gen_mishmash_name2():
    prob = random.random() * 100
    # 20% chance of english surname
    if prob <= 20:
        name = parse_english(generate_english_name2())
    # 20% chance of french surname
    elif prob <= 40:
        name = parse_french(generate_french_name2())
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

generate_mishmash_name = define_generate_language(parse_english, gen_mishmash_name1, gen_mishmash_name2)

# -----------------------------
#           Human Names
# -----------------------------

def generate_human_name():
    generators = [generate_french_name, generate_english_name, generate_mishmash_name]
    return random.choice(generators)()

