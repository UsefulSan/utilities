import os
from pathlib import Path


def get_new_filename(path):
    # if isinstance(path, str):

    if type(path) == str:
        path = Path(path)
    if not os.path.exists(os.path.join(path.parent, path.name)):
        return path
    else:
        numb = 1
        while True:
            new_path = path.parent / f'{path.stem}_{numb}{path.suffix}'
            if not os.path.exists(new_path):
                return new_path
            numb += 1
