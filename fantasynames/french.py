from fantasynames.data import french_data
from fantasynames.helpers import define_parse_string, gen_from_table
import random

# -----------------------------
#           French Names
# -----------------------------
parse_french = define_parse_string(french_data['patterns'])

def generate_french_name1():
    '''
    Outputs a randomized "French" name. Example outputs:
    'Lureit', 'Isera', 'Clesont', 'Ileau', 'Anasande'
    '''
    name = gen_from_table(french_data['name1_col1'], french_data['name1_col2'])
    return parse_french(name).capitalize()

def generate_french_name2():
    '''
    Outputs a randomized "French" surname. Example outputs:
    'Loubec', 'Rouville', 'Collefluer', 'd'Leauvcourt', 'du Berchatel'
    '''
    name = gen_from_table(french_data['name2_col1'], french_data['name2_col2'])
    name = parse_french(name).capitalize()
    # 30% chance of d' prefix
    if random.random() * 100 <= 30:
        prefix = random.choice(french_data['name2_prefixes'])
        name = prefix + name
    return name

def generate_french_name():
    return generate_french_name1() + " " + generate_french_name2()
