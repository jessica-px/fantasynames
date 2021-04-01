'''
In this file, we store the various string arrays from which names are generated.
'''

hobbit_data = {
    'name1_col1': ['BVB', 'mVB', 'frVB', 'flVB', 'wVB', 'lVB', 'BVm'],
    'name1_col2': ['*o', '*a', '*y', '*in', '*ly', 'ius', 'lius', 'nus', 'ia', 'ina', 'emina', '*urt', 'win'],
    'name2_col1': ['berry', 'sweet', 'milk', 'honey', 'crumble', 'jiggle', 'purple', 'sneaky', 'hungry', 'rumble', 'prickle', 'butter', 'long', 'short', 'old', 'fresh', 'apple', 'poppy', 'fish', 'cream', 'wimble', 'hope', 'smoke', 'fiddle', 'tickle', 'bubble'],
    'name2_col2': ['muffins', 'cakes', 'belly', 'foot', 'bum', 'finger', 'burrow', 'toe', 'tum', 'weed', 'scone', 'biscuits', 'candles', 'treats', 'crust', 'tart', 'pipe', 'feet', 'wort', 'sticks', 'stack', 'thorp'],
    'patterns': [
        {'char': 'B', 'new_chars': ['t', 'd', 'b', 'p']},
        {'char': 'V', 'new_chars': ['i', 'o', 'a', 'u']},
    ]
}

elf_data = {
    'name1_col1': ['RA', 'gA', 'gE', 'ei', 'ai', 'ie', 'gwE', 'thE', 'A', 'E', 'fA', 'cA'],
    'name1_col2': ['drAl', 'thAn', 'vAl', 'rAth', 'thAr', 'rAn', 'rAl', 'nAl'],
    'name1_suffixes': ['a', 'ia', 'on', 'ys'],
    'name2_col2': ['Nther', 'Nion', 'Nonus', 'Niath', 'Naire', 'Nuth', 'Neus', 'Naine', 'viel'],
    'patterns': [
        {'char': 'A', 'new_chars': ['a', 'a', 'e', 'e', 'ia', 'ea', 'y']},
        {'char': 'E', 'new_chars': ['a', 'e']},
        {'char': 'N', 'new_chars': ['n', 'm', 'l', 'r']},
        {'char': 'R', 'new_chars': ['l', 'r']},
        {'char': 'M', 'new_chars': ['n', 'm']},
    ]
}

dwarf_data = {
    'name1_col1': ['TOrN', 'TOR', 'thOR', 'thOrN', 'ing', 'hOR', 'ein', 'lOrg', 'ROT', 'TrOn', 'hOT', 'bOr'],
    'name1_col2': ['gIRD', 'hIRD', 'vIRD', 'rOm', 'mAr', 'nAr', 'mIr', 'nIr', 'An', 'vAR', 'muiR', 'ean'],
    'name1_suffixes': ['a'],
    'patterns': [
        {'char': 'A', 'new_chars': ['i', 'a', 'o', 'u']}, # any vowel
        {'char': 'I', 'new_chars': ['i', 'e']}, # front vowels
        {'char': 'O', 'new_chars': ['o', 'u']}, # back vowels
        {'char': 'R', 'new_chars': ['l', 'r']}, # liquids
        {'char': 'T', 'new_chars': ['t', 'd', 'th']}, # alveolar obstruents
        {'char': 'D', 'new_chars': ['t', 'd']}, # alveolar stops
    ]
}

human_data = {
    'name1_col1': ['AR', 'kAR', 'kAs', 'rAd', 'AvIn', 'brAn', 'dAn', 'AlIn', 'frIn', 'gAn', 'hAR', 'sIg', 'sAn', 'tIm', 'sAm', 'bIn'],
    'name1_col2': ['tAn', 'RAm', 'dAn', 'wArd', 'nAr', 'wAll', 'rAth', 'ric', 'rett', 'lyn', 'mAnd', 'der'],
    'name1_suffixes': ['a', 'ia'],
    'name2_col1': [
        'white', 'red', 'black', 'grey', 'west', 'east', 'fair', 'rose', 'grave', 'wood', 'daven',
        'ast', 'avon', 'bal', 'bex', 'blen', 'brad', 'row', 'car', 'cul', 'dal', 'dun', 'dry',
        'fin', 'gart', 'gil', 'glen', 'kil', 'king', 'kirk', 'knock', 'lang', 'lock',
        'lind', 'nor', 'pen', 'pit', 'pol', 'pont', 'ply', 'strat', 'stan', 'swin',
        'tarn', 'win', 'wel', 'roy', 'grim', 'mor'
    ],
    'name2_col2': [
        'beck', 'berg', 'berry', 'bury', 'burgh', 'bourne', 'burn', 'cott', 'den', 'firth', 'ham',
        'holme', 'hurst', 'ing', 'low', 'lyn', 'mere', 'more', 'pool', 'shaw',
        'stead', 'ster', 'stow', 'ton', 'ward', 'wick', 'wich', 'worth',
        'field', 'ford', 'hill', 'dale', 'fell', 'shire', 'stein', 'rock', 'mill', 'bridge', 'son', 'bluff'
    ],
    'patterns': [
        {'char': 'I', 'new_chars': ['i', 'e', 'y']},
        {'char': 'A', 'new_chars': ['i', 'a', 'o', 'u', 'e']},
        {'char': 'R', 'new_chars': ['l', 'r']},
        {'char': 'N', 'new_chars': ['n', 'm']},
    ]
}

french_data = {
    'name1_col1': ['A', 'aNa', 'ala', 'cate', 'isA', 'lu', 'ro', 'robA', 'tho', 'si', 'arnA', 'LI', 'au', 'clA', 'mA', 'cha', 'vA', 'mAri', 'bAri'],
    'name1_col2': ['mI', 'nI', 'lI', 'mis', 'min', 'mAnt', 'LA', 'Line', 'Land', 'nier', 'bel', 'bI', 'nne', 'sAnde', 'reit', 'nette', 'tain', 'sAnt', 'cia', 'belle', 'rre', 'chiel', 'chart', 'n', 'ndri', 'ndrI', 'vier', 'vien', 'lois', 'ffrey', 'rent'],
    'name2_col1': ['nI', 'vI', 'rou', 'for', 'bAr', 'clar', 'lIv', 'lI', 'caste', 'tour', 'sAtte', 'cAlle', 'I', 'Atin', 'hAL'],
    'name2_col2': ['ville', 'val', 'blAc', 'mont', 'court', 'menil', 'chatel', 'vast', 'bec', 'dalle', 'tuit', 'fleur', 'lan'],
    'name2_prefixes': ['d\'', 'de ', 'du '],
    'patterns': [
        {'char': 'A', 'new_chars': ['a', 'e', 'i', 'o']},
        {'char': 'I', 'new_chars': ['ou', 'eau']},
        {'char': 'N', 'new_chars': ['n', 'm']},
        {'char': 'L', 'new_chars': ['l', 'r']},
    ]
}

compound_tables = {
    'nature_col1': ['green', 'mist', 'willow', 'dream', 'dusk', 'night', 'sage', 'green', 'dew', 'high', 'bright', 'cliff', 'hawk', 'wind', 'rain', 'shadow', 'sun', 'cloud', 'storm'],
    'nature_col2': ['wood', 'shade', 'glade', 'blossom', 'wing', 'vale', 'grove', 'thorn', 'bark', 'grass', 'song', 'weave', 'heart', 'whisper', 'hunter', 'root'],
    'mountain_col1': ['shield', 'deep', 'dark', 'steel', 'heavy', 'grim', 'dim', 'stout', 'battle', 'iron', 'stone', 'dust', 'mountain', 'strong', 'great', 'proud', 'brave', 'gravel'],
    'mountain_col2': ['scream', 'rage', 'grip', 'brew', 'mail', 'blaze', 'strike', 'helm', 'spear', 'beard', 'fury', 'break', 'hammer', 'brow', 'cask', 'mace', 'mead', 'pike', 'pick'],
    'generic_col1': ['ash', 'swift', 'cold', 'gold', 'silk', 'dragon', 'red', 'lion', 'glory', 'black', 'blue', 'hell', 'demon', 'fire', 'wine'],
    'generic_col2': ['bane', 'scar', 'mark', 'shine', 'stride', 'brand', 'river', 'rider', 'crest', 'blade', 'bluff', 'blood', 'cloak', 'born', 'sworn', 'fist', 'ship', 'arm', 'gaze'],
}