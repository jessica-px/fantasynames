from fantasynames.data import elf_data, compound_tables
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Elf Names
# -----------------------------

transform_elf = define_transform_function(elf_data['transformations'])

def gen_elf_name1():
    '''
    Outputs a randomized "elf" name. Example outputs:
    'Ievel', 'Farathon', 'Aidrala', 'Carylon', 'Gwethara'
    '''
    name = gen_from_table(elf_data['name1_col1'], elf_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(elf_data['name1_suffixes'])

    return transform_elf(name).capitalize()

def gen_elf_name2():
    '''
    Outputs a randomized "elf" surname. Example outputs:
    'Sunblossom', 'Theviel', 'Fyrion', 'Ieraine', 'Willowthorn'
    '''
    # 50% chance of using a nature name VS elfy name
    if random.random() * 100 < 50:
        name = gen_from_table(elf_data['name1_col1'], elf_data['name2_col2'])
    else:
        name = gen_from_table(compound_tables['nature_col1'], compound_tables['nature_col2'])

    return transform_elf(name).capitalize()

def generate_elf_name():
    return gen_elf_name1() + " " + gen_elf_name2()
