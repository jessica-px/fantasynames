'''
In this file, we store the various string arrays from which names are generated.
'''

hobbit_data = {
    'name1_col1': ['BVB', 'mVB', 'frVB', 'flVB', 'wVB', 'lVB', 'BVm'],
    'name1_col2': ['*o', '*a', '*y', '*in', '*ly', 'ius', 'lius', 'nus', 'ia', 'ina', 'emina', '*urt', 'win'],
    'name2_col1': ['berry', 'sweet', 'milk', 'honey', 'crumble', 'jiggle', 'purple', 'sneaky', 'hungry', 'rumble', 'prickle', 'butter', 'long', 'short', 'old', 'fresh', 'apple', 'poppy', 'fish', 'cream', 'wimble', 'hope', 'smoke', 'fiddle', 'tickle', 'bubble'],
    'name2_col2': ['muffins', 'cakes', 'belly', 'foot', 'bum', 'finger', 'burrow', 'toe', 'tum', 'weed', 'scone', 'biscuits', 'candles', 'treats', 'crust', 'tart', 'pipe', 'feet', 'wort', 'sticks', 'stack', 'thorp'],
    'transformations': [
        {'input': 'B', 'outputs': ['t', 'd', 'b', 'p']},
        {'input': 'V', 'outputs': ['i', 'o', 'a', 'u']},
    ]
}

elf_data = {
    'name1_col1': ['RA', 'gA', 'gE', 'ei', 'ai', 'ie', 'gwE', 'thE', 'A', 'E', 'fA', 'cA'],
    'name1_col2': ['drAl', 'thAn', 'vAl', 'rAth', 'thAr', 'rAn', 'rAl', 'nAl'],
    'name1_suffixes': ['a', 'ia', 'on', 'ys'],
    'name2_col2': ['Nther', 'Nion', 'Nonus', 'Niath', 'Naire', 'Nuth', 'Neus', 'Naine', 'viel'],
    'transformations': [
        {'input': 'A', 'outputs': ['a', 'a', 'e', 'e', 'ia', 'ea', 'y']},
        {'input': 'E', 'outputs': ['a', 'e']},
        {'input': 'N', 'outputs': ['n', 'm', 'l', 'r']},
        {'input': 'R', 'outputs': ['l', 'r']},
        {'input': 'M', 'outputs': ['n', 'm']},
    ]
}

dwarf_data = {
    'name1_col1': ['TOrN', 'TOR', 'thOR', 'thOrN', 'ing', 'hOR', 'ein', 'lOrg', 'ROT', 'TrOn', 'hOT', 'bOr'],
    'name1_col2': ['gIRD', 'hIRD', 'vIRD', 'rOm', 'mAr', 'nAr', 'mIr', 'nIr', 'An', 'vAR', 'muiR', 'ean'],
    'name1_suffixes': ['a'],
    'transformations': [
        {'input': 'A', 'outputs': ['i', 'a', 'o', 'u']}, # any vowel
        {'input': 'I', 'outputs': ['i', 'e']}, # front vowels
        {'input': 'O', 'outputs': ['o', 'u']}, # back vowels
        {'input': 'R', 'outputs': ['l', 'r']}, # liquids
        {'input': 'T', 'outputs': ['t', 'd', 'th']}, # alveolar obstruents
        {'input': 'D', 'outputs': ['t', 'd']}, # alveolar stops
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
    'transformations': [
        {'input': 'I', 'outputs': ['i', 'e', 'y']},
        {'input': 'A', 'outputs': ['i', 'a', 'o', 'u', 'e']},
        {'input': 'R', 'outputs': ['l', 'r']},
        {'input': 'N', 'outputs': ['n', 'm']},
    ]
}

french_data = {
    'name1_col1': ['A', 'aNa', 'ala', 'cate', 'isA', 'lu', 'ro', 'robA', 'tho', 'si', 'arnA', 'LI', 'au', 'clA', 'mA', 'cha', 'vA', 'mAri', 'bAri'],
    'name1_col2': ['mI', 'nI', 'lI', 'mis', 'min', 'mAnt', 'LA', 'Line', 'Land', 'nier', 'bel', 'bI', 'nne', 'sAnde', 'reit', 'nette', 'tain', 'sAnt', 'cia', 'belle', 'rre', 'chiel', 'chart', 'n', 'ndri', 'ndrI', 'vier', 'vien', 'lois', 'ffrey', 'rent'],
    'name2_col1': ['nI', 'vI', 'rou', 'for', 'bAr', 'clar', 'lIv', 'lI', 'caste', 'tour', 'sAtte', 'cAlle', 'I', 'Atin', 'hAL'],
    'name2_col2': ['ville', 'val', 'blAc', 'mont', 'court', 'menil', 'chatel', 'vast', 'bec', 'dalle', 'tuit', 'fleur', 'lan'],
    'name2_prefixes': ['d\'', 'de ', 'du '],
    'transformations': [
        {'input': 'A', 'outputs': ['a', 'e', 'i', 'o']},
        {'input': 'I', 'outputs': ['ou', 'eau']},
        {'input': 'N', 'outputs': ['n', 'm']},
        {'input': 'L', 'outputs': ['l', 'r']},
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