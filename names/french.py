from names.data import french_data
from names.helpers import define_generate_language, define_parse_string, gen_from_table
import random

# -----------------------------
#           French Names
# -----------------------------
parse_french = define_parse_string(french_data['patterns'])

def generate_french_name1():
    name = gen_from_table(french_data['name1_col1'], french_data['name1_col2'])
    return parse_french(name)

def generate_french_name2():
    name = gen_from_table(french_data['name2_col1'], french_data['name2_col2'])
    # 30% chance of d' prefix
    if random.random() * 100 <= 30:
        prefix = random.choice(french_data['name2_prefixes'])
        name = prefix + name
    return parse_french(name)

def generate_french_name():
    return generate_french_name1() + " " + generate_french_name2()