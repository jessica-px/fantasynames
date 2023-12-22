# Transformation Guide

String **transformations** are exactly what they sound like -- we take an input string, transform it, and return something different. This idea draws heavily from the notion of [phonological rules](https://en.wikipedia.org/wiki/Phonological_rule), but you don't need to read that Wikipedia page to follow along. What we're doing is far simpler than that ;)

In this library, **transformations** are defined as dictionaries, which, at their simplest, contain the following fields:

- Input: The character upon which this transformation should be performed.
- Outputs: An array of strings from which we will randomly select a replacement for the Input.

For example:

```python
new_transformation = {
    'input': 'A',
    'outputs': ['a', 'e', 'i', 'o', 'u']
}
```

This transformation tells us to replace all instances of the character `'A'` with any other vowel letter. So you can think of `'A'` as a variable that just means "any vowel". The choice of character is arbitrary -- we could just as easily use `'X'` or `'9'` or '`&'`. But I think `'A'` feels intuitive here.

If we were to perform this transformation on the string `'bAn'`, we would expect the result to be one of the following: `'ban'`, `'ben'`, `'bin'`, `'bon'`, or `'bun'`.

But right now this transformation is just a dictionary -- it doesn't do anything yet. Below, we'll cover the necessary steps to implement functional transformations.

## 1. Define the transformations

Let's walk through how we might add transformations to the snake language we made in the [How to Add a New Name Generator Guide](new-generator-guide.md). First, we need to decide what these transformations will be. Let's revisit one of the tables we created:

| name1_col1 | name1_col2 |
|------------|------------|
| si         | sasa       |
| sha        | la         |
| ssi        | lisus      |
| sse        | shass      |

Now that we're thinking with transformations, we can find ways to simplify this. For example, `'ssi'` and `'sse'` differ only by one vowel -- maybe instead we should just use something like `'ssE'`, where `'E'` can be replaced by either `'a'`, `'e'`, or `'i'` (these are, in my opinion, snake-y sounding vowels). That would require a transformation like this:

```python
{
    'input': 'E',
    'outputs': ['a', 'e', 'i'],
}
```

And I see another way we could simplify our table. Snake languages should have a lot of S's, in my opinion, which is why I added both `'si'` and `'ssi'`. In my mind, `'s'` and `'ss'` should be basically interchangable with each other. That's something we could capture with a transformation! And in fact, why not throw other snake-y consonants in there, like `sh` and `z`? This could give us a transformation like this:

```python
{
    'input': 'S',
    'outputs': ['s', 'ss', 'z', 'zz', 'sh'],
}
```
Note that while the input must always be _one character_ the output can absolutely be more than one character.

Now let's actually write this code somewhere. As a convention, we prefer to store our transformations in the same dictionary we keep our tables, within `data.py`. So for our snake language, we should update that file to look like this:

```python
# data.py

snake_data = {
    'name1_col1': ['si', 'sha', 'ssi', 'sse'],
    'name1_col2': ['sasa', 'la', 'lisus', 'shass'],
    'name2_col1': ['poison', 'death', 'blood', 'night'],
    'name2_col2': ['tongue', 'scale', 'fang', 'tail'],
    'transformations': [
        {
            'input': 'E',
            'outputs': ['a', 'e', 'i'],
        },
        {
            'input': 'S',
            'outputs': ['s', 'ss', 'z', 'zz', 'sh'],
        }
    ]
}
```

Our transformations have successfully been defined! But we're still not quite ready to _do_ them yet...

## 2. Update the input tables

Our transformations only work on specific characters (let's try to keep them in caps by convention), so now we need to update our tables.

With these transformations in mind, I want my new table to look like this:

| name1_col1 | name1_col2 |
|------------|------------|
| SE         | SESE       |
|            | lE         |
|            | lEsus      |
|            | SES        |

Which would make our entry in `data.py` look like this:

```python
# data.py

snake_data = {
    'name1_col1': ['SE'],
    'name1_col2': ['SESE', 'lE', 'lEsus', 'SES'],
    'name2_col1': ['poison', 'death', 'blood', 'night'],
    'name2_col2': ['tongue', 'scale', 'fang', 'tail'],
    'transformations': [
        {
            'input': 'E',
            'outputs': ['a', 'e', 'i'],
        },
        {
            'input': 'S',
            'outputs': ['s', 'ss', 'z', 'zz', 'sh'],
        }
    ]
}
```

Once we apply our transformations, this new table will not only generate all the same things the old table did, but it'll also provide _way_ more than that.

Just as an example, `'SE'` has 15 different possible results, and `'SES'` has _75_. When we combine them, that's _1125_ different possible names. From just five letters! Even if we combined `'SE'` and `'SES'` fifty times, we probably wouldn't get any repeats. I won't list all of them here, but here are a few variants we might expect to see: `'Sassez', 'Shezis', 'Zazzesh', 'Shassazz', 'Ssiziss'`.

Very snake-y. But this is still theoretical, because we're not actually _doing_ any transformations yet...

## 3. Assigning the transformations to our class

Back in our `Snake` class in `snake.py`, we need to tell the class which transformations to use. Our parent `Language` class possesses an attribute called `transformations` that by default is an empty list `[]`, but if we override that, the class will perform the given transformations on our names.

Here's how the file will look:

```python
# snake.py
from fantasynames.languages.language import Language
from fantasynames.data import snake_data


class Snake(Language):
    transformations = snake_data["transformations"]  # <--- this is what we added!

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

Now whenever we call `Snake.name()`, it will _automatically_ apply these tranformations to both the first and last names.

And that's it, we've added transformations to our snake name generator! Now it will generate an unfathomably huge number of snake-y names, with relatively little input data.
