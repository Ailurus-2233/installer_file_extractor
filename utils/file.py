import shutil
import os

def write(info, file_path):
    '''
    文件写入操作
    '''
    with open(file_path, "w", encoding="UTF-16") as f:
        f.write(info)


def append(info, file_path):
    '''
    文件追加写入操作
    '''
    with open(file_path, "a", encoding="UTF-16") as f:
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