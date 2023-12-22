# How to Add a New Name Generator

## 1. Come up with some tables

At their most basic, the names we generate can be visualized as tables from which we randomly smash together items in different columns. So, let's say we want to make a naming language for evil snake people. We might envision tables like this:

| name1_col1 | name1_col2 |
|------------|------------|
| si         | sasa       |
| sha        | la         |
| ssi        | lisus      |
| sse        | shass      |

| name2_col1 | name2_col2 |
|------------|------------|
| poison     | tongue     |
| death      | scale      |
| blood      | fang       |
| night      | tail       |

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

## 3. Create a python module and Language subclass

Inside the `fantasynames` directory, let's create a file for our new name generator. Since it's a snake language, we'll simply call it `snake.py`.

Our snake name generator will be subclassed from the `Language` class, which comes pre-baked with a lot of the logic we'll be needing. We only have to override a few methods and everything should Just Work. Here's a basic template:

```python
# snake.py
from fantasynames.languages.language import Language


class Snake(Language):

    @classmethod
    def _name1_male(self) -> str:

    # this should return a male first name

    @classmethod
    def _name1_female(self) -> str:

    # this should return a female first name

    @classmethod
    def _name2(self) -> str:
# this should return a surname

```

## 4. Write name generating logic

Let's flesh out those methods in `snake.py`. We want them to randomly pull from the tables we defined in `data.py` -- luckily, since this is an operation we do frequently in this codebase, there's already a helper method baked into the class to make this easier! If you pass `self._name_from_lists` a list of lists, it will randomly select a string from each one and give you the combined result.

For simplicity, let's say these snake people don't have gendered names. So `_name1_female()` will just return the same thing as `_name1_male()`.

```python
# snake.py
from fantasynames.languages.language import Language
from fantasynames.data import snake_data


class Snake(Language):

    @classmethod
    def _name1_male(self) -> str:
        return self._name_from_lists([snake_data["name1_col1"], snake_data["name1_col2"]])

    @classmethod
    def _name1_female(self) -> str:
        return self._name1_male()

    @classmethod
    def _name2(self) -> str:
        return self._name_from_lists([snake_data["name2_col1"], snake_data["name2_col2"]])
```

Now our name generator is fully functional! Because these are [class methods](https://pythonbasics.org/classmethod/), we don't even need to instantiate the class to use it. We can just call `Snake.name()` and it'll use the methods we just defined to give us the kind of outputs we wanted: `Silisus Poisonfang`, `Ssela Bloodscale`, `Ssisasa Deathtongue`, etc.

And don't worry about capitalization -- the `Language` class takes care of that step for us in its `_capitalize()` method.

## 5. Add function to `__init__.py`

The users of this library won't have easy access to this method until we add an import to `fantasynames/__init__.py`. To make everything extra convenient, we'll assign the method to a variable at the bottom of our module, like this:

```python
# snake.py
from fantasynames.languages.language import Language
from fantasynames.data import snake_data


class Snake(Language):


# content removed for brevity

snake = Snake.name()  # <-- this is what we're adding
```

Then we can import it in `__init__.py` like this:

```python
# __init__.py
from fantasynames.snake import snake
```

## 6. Test it out!

Users of this library should now be able to use this method as follows:

```python
import fantasynames as names

print(names.snake())
# Possible output: `Silisus Poisonfang`, `Ssela Bloodscale`, `Ssisasa Deathtongue`, etc
```

Go ahead and test this out in the Python shell to make sure it works.

## 6. Update `README.md`

`README.md` contains examples of all of the name-generating functions that we want exposed to our users -- which includes the one we just made! Be sure to add your new function to the list so everyone knows it exists.

## 7. Done! Or are we...?

We have successfully implemented a basic name generator -- but I'm sure you can imagine ways to increase the complexity. We might use different logic for generating male or female names, or have completely different tables that we draw from at random. Go ahead and look at some of the existing name generators for inspiration!

This library also has a concept of **transformations**, which are pre-defined string patterns that can make your name generation significantly more dynamic. You can read more about this in the [transformation guide](transformation-guide.md).
