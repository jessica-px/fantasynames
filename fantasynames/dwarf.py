from fantasynames.data import dwarf_data, compound_tables
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Dwarf Names
# -----------------------------

transform_dwarf = define_transform_function(dwarf_data['transformations'])

def gen_dwarf_name1():
    '''
    Outputs a randomized "dwarf" first name. Example outputs:
    'Thormer', 'Hothvirda', 'Burmir', 'Ingvola', 'Einrom'
    '''
    name = gen_from_table(dwarf_data['name1_col1'], dwarf_data['name1_col2'])
    # 30% chance of adding a suffix
    if random.random() * 100 < 30:
        name += random.choice(dwarf_data['name1_suffixes'])
    return transform_dwarf(name).capitalize()

def gen_dwarf_name2():
    '''
    Outputs a randomized "dwarf" surname. Example outputs:
    'Stonespear', 'Steelbrow', 'Ironmead', 'Proudhelm', 'Battlemace'
    '''
    name = gen_from_table(compound_tables['mountain_col1'], compound_tables['mountain_col2'])
    return name.capitalize()

def generate_dwarf_name():
    return gen_dwarf_name1() + " " + gen_dwarf_name2()
