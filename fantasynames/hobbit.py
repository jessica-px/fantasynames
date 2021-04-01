from fantasynames.data import hobbit_data
from fantasynames.helpers import define_parse_string, gen_from_table
import random

# -----------------------------
#           Hobbit Names
# -----------------------------

parse_hobbit = define_parse_string(hobbit_data['patterns'])

def gen_hobbit_name1():
    '''
    Outputs a randomized "hobbit" name. Example outputs:
    'Wuddin', 'Flobina', 'Mablius', 'Loddly', 'Fruppo'
    '''
    name = gen_from_table(hobbit_data['name1_col1'], hobbit_data['name1_col2'])
    return parse_hobbit(name).capitalize()

def gen_hobbit_name2():
    '''
    Outputs a randomized "hobbit" surname. Example outputs:
    'Applefeet', 'Honeybiscuits', 'Rumbletum', 'Wimblepipe', 'Fiddlefoot'
    '''
    name = gen_from_table(hobbit_data['name2_col1'], hobbit_data['name2_col2'])
    return parse_hobbit(name).capitalize()

def generate_hobbit_name():
    return gen_hobbit_name1() + " " + gen_hobbit_name2()