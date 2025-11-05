from pathlib import Path
import os
# BASE_DIR = Path(__file__).parent.parent
BASE_DIR = Path.cwd().parent
# print(BASE_DIR)
all_folders = [k.name for k in BASE_DIR.iterdir() if k.is_dir()]
all_files = [k.name for k in BASE_DIR.iterdir() if k.is_file() and k.suffix == '.log']
print(*all_folders, sep='\n')
# print(*all_files, sep='\n')

# print(Path.home()) base directy of the current user

# log_file_folder = BASE_DIR.joinpath('logs')
log_file_folder = Path(BASE_DIR, 'logs')
# file_name = 'collect_gw{}.log'
counter = 0
file_collector = []
while True:
    path_ = Path(log_file_folder, f'collect_gw{counter}.log')
    if path_.exists():
        file_collector.append(path_)
    else:
        break
    counter += 1

# print(file_collector)


""" Create a new folder """

# current_path = Path(__file__).parent
# new_folder = Path(current_path, 'new_folder')
# new_folder.mkdir(exist_ok=True)
# new_folder_hierarchy = Path(current_path, new_folder, 'new_folder_1', 'new_folder_2')
# new_folder_hierarchy.mkdir(exist_ok=True, parents=True)


""" Find specific files inside the directory (eg., all files ending with .log"""
all_logs = []
for dir_path, folders, files in os.walk(str(BASE_DIR)):
    for file_name in files:
        if file_name.endswith('.log'):
            all_logs.append(Path(dir_path, file_name))
print(*all_logs, sep='\n')