import os
from pathlib import Path
import shutil
import sys


FILES_DATA = {
    "audio": ['mp3', 'ogg', 'wav', 'amr'],
    "documents": ['doc', 'txt', 'pdf', 'xlsx', 'pptx', 'docx'],
    "images": ['jpeg', 'jpg', 'svg', 'png'],
    "archives": ['zip', 'gz', 'tar'],
    "video": ['avi', 'mp4', 'mov', 'mkv'],
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for a, b in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(a)] = b
    TRANS[ord(a.upper())] = b.upper()

directory = sys.argv[1]


def normalize(name):
    split_name = name.split('.')
    split_prefix = list(split_name[0])

    for idx, letter in enumerate(split_prefix):
        char = ord(letter)

        if char in TRANS:
            split_prefix[idx] = TRANS[char]
        elif not letter.isnumeric() and char not in range(65, 91) and char not in range(97, 123):
            split_prefix[idx] = '_'

    if len(split_name) == 1:
        return "".join(split_prefix)
    else:
        return f'{"".join(split_prefix)}.{split_name[-1]}'


def create_folder(path, name):
    os.makedirs(f"{path}\\{name}", exist_ok=True)


def sort_folder(folder_path):
    path = Path(folder_path)

    for file in path.iterdir():
         if len(file.name.split('.')) < 2 and not file.is_dir():
            continue

         for type in FILES_DATA:
            if file.name.split('.')[-1].lower() in FILES_DATA[type]:
                create_folder(path, type)  
                if type == "archives":
                    normalized_name = normalize(file.name)  
                    archive_name = normalized_name.split('.')[0]
                    shutil.unpack_archive(f"{path}\\{file.name}",f"{path}\\{type}\\{archive_name}")
                else:
                    normalized_name = normalize(file.name)   
                    shutil.move(f"{path}\\{file.name}",f"{path}\\{type}\\{normalized_name}")

            if file.is_dir():  
                if len(os.listdir(file)) == 0:
                    os.rmdir(file)   
                if file.name not in FILES_DATA and file.exists():
                    normalized_name = normalize(file.name)
                    sort_folder(file) 
                    os.rename(file, f"{path}\\{normalized_name}" )
              
                          
                   
try:
    sort_folder(directory)
except FileNotFoundError:
    print("This folder doesn't exist. Enter the correct path, please.")