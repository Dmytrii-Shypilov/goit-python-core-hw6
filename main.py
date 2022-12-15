import os
import shutil
import sys
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
    
for a, b in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(a)] = b
    TRANS[ord(a.upper())] = b.upper()

def normalize(name):
    split_name = name.split('.')
    split_prefix = list(split_name[0])

    for idx, letter in enumerate(split_prefix):
        char = ord(letter)

        if char in TRANS:
            split_prefix[idx] = TRANS[char]
        elif not letter.isnumeric() and char not in range(65,91) and char not in range(97,123):
            split_prefix[idx] = '_'

    return f'{"".join(split_prefix)}.{split_name[1]}'

# list = []
normalize("НоDtt!Ини23--.mp3")
# folder = sys.argv[1]

# path = Path('D:\\python-practice')

# for i in path.iterdir():
#     if i.is_file():
#         list.append(i.name)
#         print(i)
#     if i.name == 'Alan_Walker-Faded_(2016).mp3':
#         pass
#         # os.remove(f'{path}\\{i.name}')
# print(list, len(list))
