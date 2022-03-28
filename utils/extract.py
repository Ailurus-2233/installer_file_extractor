from pathlib import Path
import utils.uniextract as uu
import utils.file as uf
from utils.log import log
from func_timeout import func_set_timeout, FunctionTimedOut
import os
import math
from config import temp_path


@func_set_timeout(800)
def run_extract_5(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(400)
def run_extract_4(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(200)
def run_extract_3(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(100)
def run_extract_2(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(50)
def run_extract_1(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


func_extract = {
    0: run_extract_1,
    1: run_extract_2,
    2: run_extract_3,
    3: run_extract_4,
    4: run_extract_5
}


def run_extract(file_path: Path, extract_path: Path):
    file_size = int(math.log(os.stat(file_path).st_size / 1024 / 1024))
    file_size = 4 if file_size >= 4 else file_size
    file_size = 0 if file_size <= 0 else file_size
    func_extract[file_size](file_path, extract_path)


def extract_root(file_path: Path, extract_path: Path):
    _, flag = uu.check_extract_path(file_path, extract_path)
    if not flag:
        uf.backup(file_path)
        try:
            run_extract(file_path, extract_path)
        except FunctionTimedOut:
            uu.extract_time_out()
        except FileNotFoundError:
            log.error(f"File not found {file_path}")
        if not file_path.exists():
            uf.restore(file_path)
        uf.remove_file(str(file_path)+".bak")


def extract_sub(file_path: Path, extract_path: Path):
    _, flag = uu.check_extract_path(file_path, extract_path)
    if not flag:
        try:
            run_extract(file_path, extract_path)
        except FunctionTimedOut:
            uu.extract_time_out()
        except FileNotFoundError:
            log.error(f"File not found {file_path}")
        _, flag = uu.check_extract_path(file_path, extract_path)
        if flag:
            return file_path.name
        return None


def extract_sub_temp(file_path: Path, root_extract_path: Path):
    temp = Path(temp_path)/file_path.name
    temp_ext = temp.parent/temp.stem
    if not temp.exists():
        uf.copy(file_path, temp)
    extract_root(temp, temp_ext)
    
    uf.remove_file(temp)
    temp_ext, flag = uu.check_extract_path(temp, temp_ext)

    if flag:
        uf.classify_file(temp_ext)
        for tp in temp_ext.iterdir():
            for file in tp.iterdir():
                uf.move(file, root_extract_path/tp.name)
        uf.remove_empty_folder(Path(temp_path))