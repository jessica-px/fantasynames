# Fantasy Name Generator

A random name generator that produces names aligning (more or less) with common conventions for fantasy characters in fictional media such as Dungeons and Dragons or World of Warcraft.

## Installation

`python3 -m pip install fantasynames`

## Usage

The following name generating functions are provided for a variety of different stereotypical fantasy "races", as well as a few different "medieval-y" languages:

```python
import fantasynames as names

names.elf()
# Example outputs: 'Farathia Eaviel', 'Iethian Willowblossom'

names.dwarf()
# Example outputs: 'Thrunnor Ironfury', 'Lothuna Strongmail'

names.hobbit()
# Example outputs: 'Libby Honeyfoot', 'Flublius Sweetscone'

names.french()
# Example outputs: 'Auland Roublac', 'Rondri de Clardalle'

names.anglo()
# Example outputs: 'Brandin of Avonlyn', 'Kallem Davenmere'

names.human()
# Example outputs: 'Danric du Tourbloc', 'Sumia Sageholme'
```

Note that `human()` provides a diverse mix of different first and last name styles, including `anglo()` and `french()`...and more!

## Adding Languages

Want to fork this repo and use it to generate your own weird fantasy names? Or even better -- want to open a PR and contribute to this repo?

Check out the [How to Add a New Name Generator Guide](docs/new-generator-guide.md). And then if you want to ramp up the complexity, take a look at the [Transformation Guide](docs/transformation-guide.md).