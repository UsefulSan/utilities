import os
from pathlib import Path


def get_new_filename(path: str | Path) -> Path:
    """
    Создает путь и новое не занятое имя для файла
    :param path: путь к файлу в виде строки или path
    :return: путь
    """
    if isinstance(path, str):
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
