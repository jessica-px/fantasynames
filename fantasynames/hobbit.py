from fantasynames.data import hobbit_data
from fantasynames.helpers import define_transform_function, gen_from_table
import random

# -----------------------------
#           Hobbit Names
# -----------------------------

transform_hobbit = define_transform_function(hobbit_data['transformations'])

def gen_hobbit_name1():
    '''
    Outputs a randomized "hobbit" name. Example outputs:
    'Wuddin', 'Flobina', 'Mablius', 'Loddly', 'Fruppo'
    '''
    name = gen_from_table(hobbit_data['name1_col1'], hobbit_data['name1_col2'])
    return transform_hobbit(name).capitalize()

def gen_hobbit_name2():
    '''
    Outputs a randomized "hobbit" surname. Example outputs:
    'Applefeet', 'Honeybiscuits', 'Rumbletum', 'Wimblepipe', 'Fiddlefoot'
    '''
    name = gen_from_table(hobbit_data['name2_col1'], hobbit_data['name2_col2'])
    return transform_hobbit(name).capitalize()

def generate_hobbit_name():
    return gen_hobbit_name1() + " " + gen_hobbit_name2()