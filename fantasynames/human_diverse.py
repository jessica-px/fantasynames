from fantasynames.data import human_data, compound_tables
from fantasynames.helpers import gen_from_table
from fantasynames.french import generate_french_name1, generate_french_name2
from fantasynames.anglo import generate_anglo_name1, generate_anglo_name2
import random

# -----------------------------
#           Human Mishmash Names
# -----------------------------

def gen_mishmash_name1():
    '''
    Outputs a randomized "human" name, which will be either "French" or "Anglo".
    '''
    # 80% chance anglo name, 20% chance french
    if random.random() * 100 <= 20:
        name = generate_french_name1()
    else:
        name = generate_anglo_name1()
    return name

def gen_mishmash_name2():
    '''
    Outputs a randomized "human" surname, which will be either "French", "Anglo", or cobbled together from various tables.
    '''
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
        name = gen_from_table(col1, col2).capitalize()

    return name

def generate_human_name():
    return gen_mishmash_name1() + " " + gen_mishmash_name2()
