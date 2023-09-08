# import os
#
#
# def get_new_filename(path):
#     if type(path) == str:
#         path = os.path.normpath(path)
#         print(type(path))
#     if not os.path.exists(path):
#         return path
#     else:
#         numb = 1
#         while True:
#             new_path = f'{path.parent}\\{path.stem}_{numb}{path.suffix}'
#             if not os.path.exists(new_path):
#                 return new_path
#             numb += 1
#
# get_new_filename('D:/Данные со старого диска/работа/ООО Тепло/Устав/Устав ЮЛ/123.docx')

import os
from pathlib import Path


def get_new_filename(path):
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


new_name = get_new_filename('D:/Данные со старого диска/работа/ООО Тепло/Устав/Устав ЮЛ/123.docx')
print(new_name)