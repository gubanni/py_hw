import os
from pathlib import Path


def group_rename(extension: str, new_extension: str, new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0]}_{new_name}_{count}.{new_extension}")