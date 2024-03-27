import typing as t

"""
In this file, we store the various string arrays from which names are generated.
"""

hobbit_data: t.Dict[str, t.List] = {
    "name1_col1": [
        "BVB",
        "mVB",
        "frVB",
        "flVB",
        "wVB",
        "lVB",
        "BVm",
        "bilb",
        "BarB",
        "mar",
    ],
    "name1_female_suffixes": ["*a", "*y", "*ia", "lia", "ina", "emina"],
    "name1_male_suffixes": [
        "*o",
        "*y",
        "*ly",
        "*in",
        "win",
        "ius",
        "lius",
        "nus",
    ],
    "name2_col1": [
        "berry",
        "sweet",
        "milk",
        "honey",
        "crumble",
        "jiggle",
        "purple",
        "sneaky",
        "hungry",
        "rumble",
        "prickle",
        "butter",
        "long",
        "short",
        "old",
        "fresh",
        "apple",
        "poppy",
        "fish",
        "cream",
        "wimble",
        "hope",
        "smoke",
        "fiddle",
        "tickle",
        "bubble",
        "brandy",
    ],
    "name2_col2": [
        "muffins",
        "cakes",
        "belly",
        "foot",
        "bum",
        "finger",
        "burrow",
        "toe",
        "tum",
        "weed",
        "scone",
        "biscuits",
        "candles",
        "treats",
        "crust",
        "tart",
        "pipe",
        "feet",
        "wort",
        "sticks",
        "stack",
        "thorp",
        "buck",
    ],
    "transformations": [
        {"input": "B", "outputs": ["t", "d", "b", "p"]},
        {"input": "V", "outputs": ["i", "o", "a", "u"]},
    ],
}

elf_data: t.Dict[str, t.List] = {
    "name1_col1": [
        "RA",
        "gA",
        "gE",
        "ei",
        "ai",
        "ie",
        "gwE",
        "thE",
        "A",
        "E",
        "fA",
        "cA",
    ],
    "name1_col2": ["drAl", "thAn", "vAl", "rAth", "thAr", "rAn", "rAl", "nAl"],
    "name1_female_suffixes": ["a", "ia", "ys", "yn"],
    "name2_col2": [
        "Nther",
        "Nion",
        "Nonus",
        "Niath",
        "Naire",
        "Nuth",
        "Neus",
        "Naine",
        "viel",
    ],
    "transformations": [
        {"input": "A", "outputs": ["a", "a", "e", "e", "ia", "ea", "y"]},
        {"input": "E", "outputs": ["a", "e"]},
        {"input": "N", "outputs": ["n", "m", "l", "r"]},
        {"input": "R", "outputs": ["l", "r"]},
        {"input": "M", "outputs": ["n", "m"]},
    ],
}

dwarf_data: t.Dict[str, t.List] = {
    "name1_col1": [
        "al",
        "an",
        "aur",
        "BAR",
        "Bil",
        "Brun",
        "Bag",
        "Ban",
        "BAn",
        "BArn",
        "eil",
        "faR",
        "ful",
        "gan",
        "gal",
        "grim",
        "gim",
        "hil",
        "lon",
        "skar",
        "vAs",
        "vin",
        "thor",
        "thor",
    ],
    "name1_col2": [
        "viss",
        "arr",
        "angr",
        "vangr",
        "urr",
        "unn",
        "dr",
        "dinn",
        "inn",
        "sten",
    ],
    "name1_col2_female": ["et", "ja", "is", "i", "ssi", "da"],
    "name1_female_suffixes": ["a"],
    "transformations": [
        {"input": "A", "outputs": ["i", "a", "o", "u"]},  # any vowel
        {"input": "R", "outputs": ["l", "r"]},
        {"input": "B", "outputs": ["b", "d", "h"]},
    ],
}

anglo_data: t.Dict[str, t.List] = {
    "name1_col1": [
        "AR",
        "kAR",
        "kAs",
        "rAn",
        "brAn",
        "dAn",
        "frEn",
        "gEn",
        "hAR",
        "sEg",
        "sAN",
        "tIm",
        "bEn",
        "As",
    ],
    "name1_col2": [
        "An",
        "RAm",
        "lAn",
        "nAr",
        "rAth",
        "ric",
        "ret",
        "lyn",
        "mAnd",
        "der",
        "win",
    ],
    "name1_male_suffixes": [
        "ARt",
        "wArd",
        "son",
        "on",
        "fried",
        "wAll",
        "hardt",
        "aRd",
        "ey",
        "duin",
        "ly",
    ],
    "name1_female_suffixes": ["a", "ia", "ie", "isa"],
    "name2_col1": [
        "white",
        "red",
        "black",
        "grey",
        "west",
        "east",
        "fair",
        "rose",
        "grave",
        "wood",
        "daven",
        "ast",
        "avon",
        "bal",
        "bex",
        "blen",
        "brad",
        "row",
        "car",
        "cul",
        "dal",
        "dun",
        "dry",
        "fin",
        "gart",
        "gil",
        "glen",
        "kil",
        "king",
        "kirk",
        "knock",
        "lang",
        "lock",
        "lind",
        "nor",
        "pen",
        "pit",
        "pol",
        "pont",
        "ply",
        "strat",
        "stan",
        "swin",
        "tarn",
        "win",
        "wel",
        "roy",
        "grim",
        "mor",
    ],
    "name2_col2": [
        "beck",
        "berg",
        "berry",
        "bury",
        "burgh",
        "bourne",
        "burn",
        "cott",
        "den",
        "firth",
        "ham",
        "holme",
        "hurst",
        "ing",
        "low",
        "lyn",
        "mere",
        "more",
        "pool",
        "shaw",
        "stead",
        "ster",
        "stow",
        "ton",
        "ward",
        "wick",
        "wich",
        "worth",
        "field",
        "ford",
        "hill",
        "dale",
        "fell",
        "shire",
        "stein",
        "rock",
        "mill",
        "bridge",
        "son",
        "bluff",
    ],
    "transformations": [
        {"input": "E", "outputs": ["a", "i", "e"]},
        {"input": "I", "outputs": ["i", "e", "y"]},
        {"input": "A", "outputs": ["i", "a", "o", "u", "e"]},
        {"input": "R", "outputs": ["l", "r"]},
        {"input": "N", "outputs": ["n", "m"]},
    ],
}

french_data: t.Dict[str, t.List] = {
    "name1_col1": [
        "IN",
        "IB",
        "Il",
        "aB",
        "Is",
        "RuB",
        "RIB",
        "sIB",
        "arn",
        "auB",
        "clIB",
        "BIR",
        "jul",
        "vic",
    ],
    "name1_col2": [
        "ton",
        "is",
        "En",
        "Ant",
        "And",
        "ieR",
        "el",
        "Irt",
        "ois",
        "et",
        "ert",
        "ard",
    ],
    "name1_female_suffixes": [
        "*a",
        "ia",
        "*e",
    ],
    "name1_male_suffixes": [
        "d#ré",
        "eau",
        "aise",
        "r#ien",
        "ein",
        "erré",
        "ain",
    ],
    "name2_col1": [
        "nI",
        "vI",
        "rou",
        "for",
        "bAr",
        "clar",
        "lIv",
        "lI",
        "caste",
        "tour",
        "sAtte",
        "cAlle",
        "I",
        "Atin",
        "hAL",
    ],
    "name2_col2": [
        "ville",
        "val",
        "blAc",
        "mont",
        "court",
        "menil",
        "chatel",
        "vast",
        "bec",
        "dalle",
        "tuit",
        "fleur",
        "lan",
    ],
    "name2_prefixes": ["d'", "de ", "du "],
    "transformations": [
        {"input": "A", "outputs": ["a", "e", "i", "o", "u"]},
        {"input": "I", "outputs": ["e", "a", "i"]},
        {"input": "N", "outputs": ["n", "m"]},
        {"input": "L", "outputs": ["l", "r"]},
        {"input": "B", "outputs": ["l", "r", "m", "n", "c", "ch", "v", "s"]},
    ],
}

compound_tables: t.Dict[str, t.List] = {
    "nature_col1": [
        "green",
        "mist",
        "willow",
        "dream",
        "dusk",
        "night",
        "sage",
        "green",
        "dew",
        "high",
        "bright",
        "cliff",
        "hawk",
        "wind",
        "rain",
        "shadow",
        "sun",
        "cloud",
        "storm",
    ],
    "nature_col2": [
        "wood",
        "shade",
        "glade",
        "blossom",
        "wing",
        "vale",
        "grove",
        "thorn",
        "bark",
        "grass",
        "song",
        "weave",
        "heart",
        "whisper",
        "hunter",
        "root",
    ],
    "mountain_col1": [
        "shield",
        "deep",
        "dark",
        "steel",
        "heavy",
        "grim",
        "stout",
        "battle",
        "iron",
        "stone",
        "dust",
        "mountain",
        "strong",
        "great",
        "proud",
        "brave",
        "gravel",
    ],
    "mountain_col2": [
        "scream",
        "rage",
        "grip",
        "brew",
        "mail",
        "blaze",
        "strike",
        "helm",
        "spear",
        "beard",
        "fury",
        "break",
        "hammer",
        "brow",
        "cask",
        "mace",
        "mead",
        "pike",
        "pick",
    ],
    "generic_col1": [
        "ash",
        "swift",
        "cold",
        "gold",
        "silk",
        "dragon",
        "red",
        "lion",
        "glory",
        "black",
        "blue",
        "hell",
        "demon",
        "fire",
        "wine",
    ],
    "generic_col2": [
        "bane",
        "scar",
        "mark",
        "shine",
        "stride",
        "brand",
        "river",
        "rider",
        "crest",
        "blade",
        "bluff",
        "blood",
        "cloak",
        "born",
        "sworn",
        "fist",
        "ship",
        "arm",
        "gaze",
    ],
}

drow_data: t.Dict[str, t.List] = {
    "name1_col1_male": [
        "ant",
        "berg",
        "caer",
        "chel",
        "dan",
        "din",
        "dragh",
        "driz",
        "elk",
        "erth",
        "gel",
        "ghol",
        "go",
        "harn",
        "hurz",
        "ib",
        "il",
        "izz",
        "jaez",
        "jal",
        "kar",
        "kel",
        "khaz",
        "les",
        "lu",
        "mag",
        "malag",
        "moc",
        "nad",
        "nil",
        "nym",
        "orm",
        "phal",
        "phar",
        "pho",
        "quev",
        "quil",
        "rel",
        "ran",
        "ryld",
        "sav",
        "shar",
        "szin",
        "szor",
        "tin",
        "vhae",
        "xorl",
        "yaz",
        "yyrr",
        "zak"
    ],
    "name1_col2_male": [
        "agar",
        "antar",
        "arrin",
        "as",
        "atlab",
        "aun",
        "azzt",
        "daal",
        "daer",
        "diin",
        "dor",
        "dyn",
        "erd",
        "fein",
        "gos",
        "hin",
        "imar",
        "inyon",
        "kyn",
        "lyn",
        "mus",
        "nar",
        "nin",
        "olin",
        "orvir",
        "phul",
        "ral",
        "rimm",
        "rorn",
        "tak",
        "thae",
        "tos",
        "tran",
        "tyrr",
        "ven",
        "yrd",
        "yrr",
        "zaer",
        "zyn",
        "ztl"
        ],

    "name1_col1_female": [
        "alaun",
        "aun",
        "bae",
        "braer",
        "char",
        "chess",
        "daen",
        "dan",
        "dil",
        "dro",
        "elvan",
        "ethe",
        "faer",
        "filf",
        "ghuan",
        "gil",
        "har",
        "hor",
        "houn",
        "iim",
        "illiam",
        "ilph",
        "jan",
        "jhael",
        "jys",
        "kar",
        "khal",
        "kier",
        "mal",
        "micar",
        "myl",
        "nara",
        "nau",
        "ned",
        "ogg",
        "olor",
        "pera",
        "pha",
        "phaer",
        "qil",
        "quav",
        "quii",
        "rel",
        "sab",
        "shri",
        "suss",
        "szar",
        "thia",
        "triel",
        "us",
        "vas",
        "vic",
        "xan",
        "xurn",
        "yas",
        "yv",
        "zes",
        "zilv"
        ],
    "name1_col2_female": [
        "ae",
        "aer",
        "aeth",
        "afae",
        "ali",
        "anna",
        "bryn",
        "da",
        "deirra",
        "diira",
        "dryn",
        "ffyn",
        "ess",
        "eyl",
        "hyrr",
        "hea",
        "iira",
        "inil",
        "isstra",
        "jra",
        "less",
        "lur",
        "nala",
        "nei",
        "nilee",
        "noa",
        "olin",
        "onia",
        "qualyn",
        "rae",
        "raya",
        "ress",
        "riel",
        "rygg",
        "riia",
        "roth",
        "set",
        "shalee",
        "str",
        "syn",
        "thrae",
        "tree",
        "va",
        "vayas",
        "vyll"
        "wyss",
        "xena",
        "xyra",
        "yalla",
        "ynda",
        "yrr",
        "zheel",
        "zyne"
        ],
    "name2_col1": [
        "arab",
        "arken",
        "baen",
        "cladd",
        "dal",
        "de",
        "eils",
        "everh",
        "do'",
        "gode",
        "hla",
        "hun'",
        "jab",
        "kil",
        "mae",
        "my",
        "noqu",
        "oss",
        "rilyn",
        "shav",
        "stri",
        "teken'",
        "thal",
        "vi",
        "zau"
    ],
    "name2_col2": [
        "afin",
        "ar",
        "arn",
        "ate",
        "cyx",
        "duis",
        "ellar",
        "ett",
        "gar",
        "ghym",
        "hea",
        "inth",
        "luth",
        "lyl",
        "mtor",
        "muth",
        "ndar",
        "qai",
        "rae",
        "rak",
        "rimm",
        "sek",
        "th",
        "tlar",
        "tral",
        "tyl",
        "und",
        "urden",
        "val",
        "vex",
        "viir",
        "vog",
        "zynge"
    ],
}