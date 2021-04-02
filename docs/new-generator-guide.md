# How to Add a New Name Generator

## 1. Come up with some tables

At their most basic, the names we generate can be visualized as tables from which we randomly smash together items in different columns. So, let's say we want to make a naming language for evil snake people. We might envision tables like this:

| name1_col1| name1_col2  |
|-----|-------|
| si  | sasa  |
| sha | la    |
| ssi | lisus |
| sse | shass |

| name2_col1| name2_col2  |
|-----|-------|
| poison  | tongue  |
| death | scale    |
| blood | fang |
| night | tail |

By randomly picking things from column 1 and pairing them with things in column 2, we should be able to generate names like `Silisus Poisonfang`, `Ssela Bloodscale`, and `Ssisasa Deathtongue` -- seems suitable for evil snake people, right?

## 2. Put the table data in `data.py`

For consistency's sake, we store all of this string data in `fantasynames/data.py` -- especially because another name generator might one day want to reuse this table! Note that although we're thinking of them as tables, they're really just unrelated arrays stored inside of a dictionary for easy importing.

```python
# data.py

snake_data = {
    'name1_col1': ['si', 'sha', 'ssi', 'sse'],
    'name1_col2': ['sasa', 'la', 'lisus', 'shass'],
    'name2_col1': ['poison', 'death', 'blood', 'night'],
    'name2_col2': ['tongue', 'scale', 'fang', 'tail'],
}
```

Since `name2` follows a compound word pattern, we could also store its data in the already existing `compound_tables` dictionary instead. But `compound_tables` is meant for fairly generic, reusable compound names, and these names seem highly specific to snake people. So for now, there's no harm in just keeping them in `snake_data`. Use your own judgement here.

## 3. Create a python module

Inside the `fantasynames` directory, let's create a file for our new name generator. Since it's a snake language, we'll simply call it `snake.py`.

The most important thing this file will do is define the final name generating function. But it's convenient to also store helper functions here, like functions for generating first and last names. Here's an outline:

```python
# snake.py

def generate_snake_name1():
    # return a randomized first name

def generate_snake_name2():
    # return a randomized last name

def generate_snake_name():
    return generate_snake_name1() + " " + generate_snake_name2()
```

`generate_snake_name()` is the main star of this file, but the helper functions will do all the heavy lifting.

## 4. Write name generating logic

Let's flesh out those helper functions in `snake.py`. We want them to randomly pull from the tables we defined in `data.py` -- luckily, since this is an operation we do frequently in this codebase, we already have a helper function defined for that. If we pass two arrays to `gen_from_table()`, it will randomly select a string from each of them and combine them. Don't forget to capitalize your name before returning it!

```python
# snake.py
from data import snake_data
from helpers import gen_from_table

def generate_snake_name1():
    name = gen_from_table(snake_data.name1_col1, snake_data.name1_col2)
    return name.capitalize()

def generate_snake_name2():
    name = gen_from_table(snake_data.name2_col1, snake_data.name2_col2)
    return name.capitalize()

def generate_snake_name():
    return generate_snake_name1() + " " + generate_snake_name2()
```

Now our name-generating function is fully functional! If we call `generate_snake_name()` we should get outputs just like we initially predicted: `Silisus Poisonfang`, `Ssela Bloodscale`, `Ssisasa Deathtongue`, etc.

## 5. Add function to `__init__.py`

The users of this library won't have easy access to this function until we add an import to `fantasynames/__init__.py`. The convention is pretty straightforward -- import your name-generating function `as` something simple (ideally whatever you named your `.py` module). In our case, it would look like this:

```python
# __init__.py
from fantasynames.snake import generate_snake_name as snake
```

## 6. Update `README.md`

`README.md` contains examples of all of the name-generating functions that we want exposed to our users -- which includes the one we just made! Be sure to add your new function to the list.

## 7. Done! Or are we...?

We have now implemented a basic name generator! A user of this library can use our function as follows:

```python
import fantasynames as names

print(names.snake())
# Possible output: `Silisus Poisonfang`, `Ssela Bloodscale`, `Ssisasa Deathtongue`, etc
```

But we could get substantially more complex than this, if we wanted to. For one thing, I'm sure you can envision adding more logic to our name-generating helpers -- like adding a chance to draw a suffix or title from an additional array (perhaps we want to see _Lady_ Ssila Deathscale!), or perhaps using another table entirely (one for masculine names, one for feminine names?), etc.

But this library also has a concept called **transformations** that can have very dynamic impacts on the kinds of names we generate. If you're interested, read more about this in the [transformation guide](transformation-guide.md).