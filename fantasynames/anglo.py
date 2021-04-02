from fantasynames.data import human_data
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Anglo Names
# -----------------------------
transform_anglo = define_transform_function(human_data['transformations'])

def generate_anglo_name1():
    '''
    Outputs a randomized "Anglo" first name. Example outputs:
    'Senia', 'Redreth', 'Dina', 'Brun', 'Kuswall', 'Ulinworda'
    '''
    # 50% chance of only using col1
    if random.random() * 100 < 50:
        name = random.choice(human_data['name1_col1'])
    else:
        name = gen_from_table(human_data['name1_col1'], human_data['name1_col2'])
    # 50% chance of adding a suffix
    if random.random() * 100 < 50:
        name += random.choice(human_data['name1_suffixes'])
    return transform_anglo(name).capitalize()

def generate_anglo_name2():
    '''
    Outputs a randomized "Anglo" surname. Example outputs:
    'Gilmore', 'Dunstow',  'of Bradham', 'of Knockster', 'Lockshaw'
    '''
    # 50% chance to use "name1 of name2" format
    if random.random() * 100 <= 50:
        name = gen_from_table(human_data['name2_col1'], human_data['name2_col2'])
        name = transform_anglo(name).capitalize()
        return 'of ' + name
    else:
        name = gen_from_table(human_data['name2_col1'], human_data['name2_col2'])
        return transform_anglo(name).capitalize()

def generate_anglo_name():
    return generate_anglo_name1() + " " + generate_anglo_name2()
