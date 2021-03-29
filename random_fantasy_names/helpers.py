import random

'''
This file is for storing helper functions that, ideally, handle the bulk of the
repeatable logic involved in generating names.
'''

def define_parse_string(patterns):
    '''
    A HOF that, given an of array of 'pattern' dicts, returns a parse_string() function
    that operates based on that array.
    EX:
        patterns = [ {'char': 'B', 'new_chars': ['t', 'd', 'b', 'p']} ]
        b_parser = define_parse_string(patterns)
        print(b_parser('Bello B*orld'))
        # Possible Outputs: 'tello ddorld', 'dello bborld', 'pello ttorld', etc.
    '''
    def parse_string(string):
        '''
        Given a string, loops over each char. If 'char' is present in one of pre-defined
        'pattern' dicts, "replaces" it with a randomly selected character from the
        provided 'new_chars' array. Returns a new string with the newly replaced chars.
        (No actual mutations performed.)

        Also has the following special rules for special "pattern" characters:
            - *: repeat the previous character (if present)
        '''
        new_string = ''
        for char in string:
            new_char = char
            for pattern in patterns:
                if char == pattern['char']:
                    new_char = random.choice(pattern['new_chars'])
                    break
                if char == '*':
                    new_char = new_string[-1]
            new_string += new_char
        return new_string
    return parse_string

def define_generate_language(parser_func, name1_func, name2_func):
    '''
    A HOF that, given a parser function (defined with define_parse_string()) and two
    name-generating functions, returns the parsed and formatted results of both generators.
    '''
    def generate_language():
        name1 = parser_func(name1_func())
        name2 = parser_func(name2_func())
        full_name = name1 + ' ' + name2
        return full_name.title()
    return generate_language

def gen_from_table(col1, col2):
    '''
    Given two string arrays (a "left" column and a "right" column) returns a string
    concatenating a random selection from each. For brevity.
    '''
    return random.choice(col1) + random.choice(col2)
