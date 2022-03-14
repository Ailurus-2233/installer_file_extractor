import shutil
import os
from pathlib import Path
from config import ext_type_list, ext_save_list, exe_size, save_list


def write(info, file_path):
    '''
    文件写入操作
    '''
    with open(file_path, "w", encoding="UTF-8") as f:
        f.write(info)


def append(info, file_path):
    '''
    文件追加写入操作
    '''
    with open(file_path, "a", encoding="UTF-8") as f:
        f.write(info)


def move(old_path, new_path):
    shutil.move(str(old_path), str(new_path))


def remove(folder_path):
    shutil.rmtree(folder_path)


def backup(file_path):
    shutil.copyfile(file_path, str(file_path) + ".bak")


def restore(file_path):
    shutil.copyfile(str(file_path) + ".bak", file_path)


def remove_file(file_path):
    os.remove(file_path)


def get_file_list(floder_path: Path, file_list=[]):
    for f in floder_path.iterdir():
        if (floder_path / f.name).is_dir():
            get_file_list(floder_path / f.name, file_list)
        if (floder_path / f.name).is_file():
            file = floder_path / f.name
            if file.suffix in ext_type_list:
                if file.suffix in ext_save_list:
                    if file.suffix in ['.exe', '.EXE'] and os.stat(file).st_size > exe_size:
                        file_list.append(file)
                    if file.suffix in ['.msi', '.MSI']:
                        file_list.append(file)
                else:
                    file_list.append(file)
    return file_list


def remove_useless_file(floder_path: Path):
    for f in floder_path.iterdir():
        file = floder_path / f.name
        if file.is_dir():
            remove_useless_file(file)
        if file.is_file() and file.suffix not in save_list:
            remove_file(file)


def remove_empty_folder(floder_path: Path):
    for f in floder_path.iterdir():
        target = floder_path / f.name
        if target.is_dir():
            remove_empty_folder(target)
            if not os.listdir(target):
                remove(target)