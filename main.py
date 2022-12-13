import os
import shutil
import sys
from pathlib import Path

files_data = {
    "audio": {
        "files": [],
        "formats": []
    },
    "video": {
        "files": [],
        "formats": []
    },
    "images": {
        "files": [],
        "formats": []
    },
    "archives": {
        "files": [],
        "formats": []
    }
}

list = []

folder = sys.argv[1]

path = Path(folder)

for i in path.iterdir():
    if i.is_file():
        list.append(i.name)

print(list)
