import random

'''
This file is for storing helper functions that, ideally, handle the bulk of the
repeatable logic involved in generating names.
'''

def define_transform_function(transformations):
    '''
    A HOF that, given an of array of 'pattern' dicts, returns a parse_string() function
    that operates based on that array. See transformations.md for more info.
    '''
    def transform_string(string):
        '''
        Given a string, loops over each char. If 'input' is present in one of pre-defined
        'transformation' dicts, "replaces" it with a randomly selected character from the
        provided 'outputs' array. Returns a new string with the newly replaced chars.
        (No actual mutations performed.)

        Also has the following special rules for special "input" characters:
            - *: repeat the previous character (if present)
        '''
        new_string = ''
        for char in string:
            new_char = char
            for transformation in transformations:
                if char == transformation['input']:
                    new_char = random.choice(transformation['outputs'])
                    break
                if char == '*':
                    new_char = new_string[-1]
            new_string += new_char
        return new_string
    return transform_string

def gen_from_table(col1, col2):
    '''
    Given two string arrays (a "left" column and a "right" column) returns a string
    concatenating a random selection from each. For brevity.
    '''
    return random.choice(col1) + random.choice(col2)
