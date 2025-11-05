import pathlib
from pathlib import Path

current_path = Path(__file__)

BASE_DIR = current_path.parent.parent
# print(current_path)
# print(current_path.name)
# print(current_path.parts)
# print(BASE_DIR)
file_name = 'log.log'
folder_from_base_dir = ['logs', 'december']
path_to_log = pathlib.Path(BASE_DIR, *folder_from_base_dir,file_name)
print(path_to_log)

with open(path_to_log) as file:
    print(file.read())