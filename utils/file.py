import shutil
import os
from pathlib import Path
from utils.log import log
from config import save_list, file_type
import stat
from utils import extract as ue 


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
    try:
        shutil.move(str(old_path), str(new_path))
    except PermissionError:
        ue.kill_all_process()
        remove_file(str(old_path))
    except Exception:
        remove_file(str(old_path))


def copy(file, new_file):
    shutil.copyfile(file, new_file)


def remove(folder_path):
    while 1:
        if not os.path.exists(folder_path):
            break
        try:
            shutil.rmtree(folder_path)
        except PermissionError as e:
            err_file_path = str(e).split("\'", 2)[1]
            log.error(f"PermissionError: {err_file_path}")
            if os.path.exists(err_file_path):
                os.chmod(err_file_path, stat.S_IWUSR)


def backup(file_path):
    copy(file_path, str(file_path) + ".bak")


def restore(file_path):
    copy(str(file_path) + ".bak", file_path)


def remove_file(file_path):
    try:
        os.remove(file_path)
    except Exception:
        pass


def get_file_list(floder_path: Path, file_list=[], deep=0):
    if deep == 0:
        file_list = []
    for file in floder_path.iterdir():
        if file.is_dir():
            get_file_list(file, file_list, deep+1)
        else:
            file_list.append(file)
    return file_list


def remove_useless_file(floder_path: Path):
    '''
    删除无用文件
    '''
    for file in floder_path.iterdir():
        if file.is_dir():
            remove_useless_file(file)
        if file.is_file() and file.suffix not in save_list:
            remove_file(file)


def remove_empty_folder(floder_path: Path):
    '''
    删除空目录
    '''
    for file in floder_path.iterdir():
        if file.is_dir():
            remove_empty_folder(file)
            if not os.listdir(file):
                remove(file)


def load_cache_file(file_path: Path):
    '''
    载入已解压文件列表
    '''
    file = file_path.parent / f'{file_path.stem}.sf'
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


def save_cache_file(file_path: Path, save_file_list: list):
    '''
    将解压文件添加到缓存文件
    '''
    file = file_path.parent / f'{file_path.stem}.sf'
    tmp = load_cache_file(file)
    tmp.extend(save_file_list)
    tmp = list(set(tmp))
    with open(file, "w", encoding="UTF-8") as f:
        for sfile in tmp:
            f.write(str(sfile) + '\n')


def get_all_file_list(floder_path: Path, file_list=[], deep=0):
    if deep == 0:
        file_list = []
    for file in floder_path.iterdir():
        if file.is_dir():
            get_all_file_list(file, file_list, deep+1)
        if file.is_file():
            file_list.append(file)
    return file_list


def save_file_name(extract_path, deleted_list):
    file_list = get_all_file_list(extract_path)
    file_list += deleted_list
    s = ""
    for f in file_list:
        try:
            s += f'{str(f.name).split("-", 1)[1]}\n'
        except IndexError:
            s += f'{str(f.name)}\n'
    write(s, extract_path / 'filenames.txt')


def get_type_file_list(floder_path: Path, type_list, file_list=[], deep=0):
    '''
    获取特定文件类型的文件列表
    '''
    if type(type_list) == str:
        type_list = file_type[type_list]
    if deep == 0:
        file_list = []
    for file in floder_path.iterdir():
        if file.is_dir():
            get_type_file_list(file, type_list, file_list, deep+1)
        if file.is_file():
            if file.suffix in type_list:
                file_list.append(file)
    return file_list


def classify_file(floder_path: Path):
    ue.kill_all_process()
    '''
    将目标文件夹下的文件，按照文件类型分类到不同的文件夹，这些文件夹存储在target_path下
    '''
    temp_path = floder_path.parent/'temp'
    for tp in file_type.keys():
        file_list = get_type_file_list(floder_path, tp)
        (temp_path/tp).mkdir(parents=True, exist_ok=True)
        for file in file_list:
            tar_file = get_tar_file(file)
            move(file, temp_path/tp/tar_file)

    other_file_list = get_file_list(floder_path)
    (temp_path/'other').mkdir(parents=True, exist_ok=True)

    for file in other_file_list:
        tar_file = get_tar_file(file)
        move(file, temp_path/'other'/tar_file)
    remove_empty_folder(floder_path)

    for file in temp_path.iterdir():
        move(file, floder_path)
    remove(temp_path)


def get_tar_file(file):
    if str(os.stat(file).st_size) in str(file.name):
        tar_file = str(file.name)
    else:
        tar_file = f'{os.stat(file).st_size}-{str(file.name)}'
    return tar_file
