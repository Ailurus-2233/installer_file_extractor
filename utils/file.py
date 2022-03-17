import shutil
import os
from pathlib import Path

from sympy import re
from config import ext_type_list, ext_save_list, exe_size, save_list, cache_path, max_deep


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
    try:
        os.remove(file_path)
    except Exception:
        pass


def get_file_list(floder_path: Path, file_list=[], save_list=[], deep=0):
    if deep > max_deep:
        return file_list, save_list
    for f in floder_path.iterdir():
        if (floder_path / f.name).is_dir():
            get_file_list(floder_path / f.name, file_list,
                          save_list, deep=deep+1)
        if (floder_path / f.name).is_file():
            file = floder_path / f.name
            if file.suffix in ext_type_list:
                if file.suffix in ext_save_list:
                    if file.suffix in ['.exe', '.EXE'] and os.stat(file).st_size > exe_size:
                        file_list.append(file)
                    if file.suffix in ['.msi', '.MSI']:
                        file_list.append(file)
                    save_list.append(file)
                else:
                    file_list.append(file)
    return file_list, save_list


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


def load_cache_file(file_path: Path):
    file = Path(cache_path) / f'{file_path.stem}.sf'
    if not file.exists():
        return []
    with open(file, "r", encoding="UTF-8") as f:
        arr_tmp = f.readlines()
        for file in arr_tmp:
            index = arr_tmp.index(file)
            if '\n' in file:
                file = file.replace('\n', '')
            arr_tmp[index] = Path(file)
    return arr_tmp


def add_cache_file(file_path: Path, save_file_list: list):
    file = Path(cache_path) / f'{file_path.stem}.sf'
    tmp = load_cache_file(file)
    tmp.extend(save_file_list)
    tmp = list(set(tmp))
    with open(file, "w", encoding="UTF-8") as f:
        for sfile in tmp:
            f.write(str(sfile) + '\n')
