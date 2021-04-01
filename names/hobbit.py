from names.data import hobbit_data
from names.helpers import define_generate_language, define_parse_string, gen_from_table
import random

# -----------------------------
#           Hobbit Names
# -----------------------------

parse_hobbit = define_parse_string(hobbit_data['patterns'])

def gen_hobbit_name1():
    return gen_from_table(hobbit_data['name1_col1'], hobbit_data['name1_col2'])
def gen_hobbit_name2():
    return gen_from_table(hobbit_data['name2_col1'], hobbit_data['name2_col2'])

generate_hobbit_name = define_generate_language(parse_hobbit, gen_hobbit_name1, gen_hobbit_name2)
