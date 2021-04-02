# Transformation Guide

String **transformations** are exactly what they sound like -- we take an input string, transform it, and return something different. This idea draws heavily from the notion of [phonological rules](https://en.wikipedia.org/wiki/Phonological_rule), but you don't need to read that Wikipedia page to follow along. What we're doing is far simpler than that ;)

In this library, **transformations** are defined as dictionaries, which, at their simplest, contain the following fields:

- Input: The character upon which this transformation should be performed.
- Outputs: An array of strings from which we will randomly select a replacement for the Input.

For example, the following transformation tells us to replace all instances of `A` with any other vowel letter. So you can think of `A` as a variable that just means "any vowel".

```python
new_transformation = {
    'input': 'A',
    'outputs': ['a', 'e', 'i', 'o', 'u']
}
```

If we were to perform this transformation on the string `'bAn'`, we would expect the result to be one of the following: `'ban'`, `'ben'`, `'bin'`, `'bon'`, or `'bun'`.

(Note that the selection of `A` as the `input` here is arbitrary -- we could just as easily choose `E`, or `9`, or `@` -- but let's just try to stick with something relatively intuitive).

But right now this transformation is just a dictionary -- it doesn't do anything yet. Below, we'll cover the necessary steps to implement functional transformations.

## 1. Define the transformations

Let's walk through how we might add transformations to the snake language we made in the [How to Add a New Name Generator Guide](new-generator-guide.md). First, we need to decide what these transformations will be. Let's revisit one of the tables we created:

| name1_col1| name1_col2  |
|-----|-------|
| si  | sasa  |
| sha | la    |
| ssi | lisus |
| sse | shass |

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

| name1_col1| name1_col2  |
|-----|-------|
| SE  | SESE  |
|     | lE    |
|     | lEsus |
|     | SES |

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

## 3. Defining the transformer function

The actual logic of applying these transformations will be handled by our **transformer function**. As you might expect, it'll do the steps of looking at each character, checking to see if a transformation should apply to them, randomly selecting a replacement, etc. Luckily, you don't have to write all of that from scratch.

One of the helper functions in this library is named `define_transform_function()`, and it is a higher-order function that creates transformation functions. Using it is really simple -- we pass it an array of transformations, and it gives us a transformer function that will perform them on a given string. Like so:

```python
from fantasynames.data import snake_data
from fantasynames.helpers import define_transform_function

transform_snake = define_transform_function(snake_data['transformations'])
transformed_name = transform_snake('SESES')
print(transformed_name) # Possible outputs: 'Sassez', 'Shezis', 'Zazzesh', etc.
```

That's it, we're doing it! We're now applying the transformations that we defined in `data.py`, allowing this simple 5 character string to have 1125 snake-y variations.

Now we just need to add this to the actual name generating logic!

## 4. Update name generating function(s)

Let's revist `snake.py`. As it currently exists, it'll give us weird strings with capital letters mixed in like `'SESUS'` and `'SElE'`. It won't do any transformations until we add a transformer function and start using it in our name generating logic.

So, a revised edition of `snake.py` would look like this:

```python
# snake.py
from data import snake_data
from helpers import gen_from_table, define_transform_function

transform_snake = define_transform_function(snake_data['transformations'])

def generate_snake_name1():
    name = gen_from_table(snake_data.name1_col1, snake_data.name1_col2)
    return transform_snake(name).capitalize() # <-- It's import to transform it before capitalizing it, or the newly capitalized letters might get caught up in our transformations!

def generate_snake_name2():
    name = gen_from_table(snake_data.name2_col1, snake_data.name2_col2)
    return transform_snake(name).capitalize()

def generate_snake_name():
    return generate_snake_name1() + " " + generate_snake_name2()
```

That's it, we've added transformations to our snake name generator! Now it will generate an unfathomably huge number of snake-y names, with relatively little input data.
