import os
import shutil
import sys
from pathlib import Path

FORMATS = {
    "audio": ['mp3', 'ogg', 'wav', 'amr'],
    "documents": ['doc', 'txt', 'pdf', 'xlsx', 'pptx', 'docx'],
    "images": ['jpeg', 'jpg', 'svg', 'png'],
    "archives": ['zip', 'gz', 'tar'],
    "video": ['avi', 'mp4', 'mov', 'mkv']
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
    
for a, b in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(a)] = b
    TRANS[ord(a.upper())] = b.upper()

path = sys.argv[1]

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


def create_folders(path):
    for file_type in FORMATS.keys():
       os.makedirs(f"{path}\\{file_type}", exist_ok=True)
    


def sort_folder(folder_path):
    path = Path(folder_path)
   
    create_folders(path)
    for file in path.iterdir():
        if file.is_dir():
            print(file)
            sort_folder(file)
        if len(file.name.split('.')) < 2:
            continue
        if file.name.split('.')[1] in FORMATS['audio']:
            normalized_name = normalize(file.name)
            shutil.move(f"{path}\\{file.name}",f"{path}\\audio\\{normalized_name}")
        if file.name.split('.')[1] in FORMATS['video']:
            normalized_name = normalize(file.name)
            shutil.move(f"{path}\\{file.name}",f"{path}\\video\\{normalized_name}")
        if file.name.split('.')[1] in FORMATS['images']:
            normalized_name = normalize(file.name)
            shutil.move(f"{path}\\{file.name}",f"{path}\\images\\{normalized_name}")
        if file.name.split('.')[1] in FORMATS['documents']:
            normalized_name = normalize(file.name)
            shutil.move(f"{path}\\{file.name}",f"{path}\\documents\\{normalized_name}")
        if file.name.split('.')[1] in FORMATS['archives']:
            normalized_name = normalize(file.name)  
            shutil.unpack_archive(f"{path}\\{file.name}",f"{path}\\archives\\{file.name.split('.')[0]}\\{normalized_name}")
        

sort_folder(path)

# list = []
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
