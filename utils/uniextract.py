from tkinter import N
import utils.file as uf
from pathlib import Path
import os
import tempfile
import time
import psutil
from config import uniextract, uniextract_path
from utils.log import log
from config import kill_name


def add_batch_queue(file_path, extract_path):
    if extract_path != "/sub":
        info = f'"{file_path}" "{extract_path}" /silent\n'
    else:
        info = f'"{file_path}" /sub /silent\n'
    uf.append(info, uniextract_path/"batch.queue")


def run_extract(file_path, extract_path):
    kill_all_process()
    if extract_path == "/sub":
        extract_path = file_path.parent/file_path.stem
    if (Path(tempfile.gettempdir()) / file_path.stem).exists():
        uf.remove(Path(tempfile.gettempdir()) / file_path.stem)
    if extract_path.exists():
        uf.remove(extract_path)
    os.system(f'{uniextract} "{file_path}" "{extract_path}" /silent')


def check_extract_path(file_path, extract_path):
    temp_path = Path(tempfile.gettempdir()) / file_path.name
    extract_path2 = Path(str(extract_path)+"_已解包")

    flag = False
    ext_path = None

    while temp_path.exists() or (extract_path.exists() or extract_path2.exists()):
        if not (extract_path.exists() or extract_path2.exists()):
            time.sleep(1)
        if (not temp_path.exists()) and (extract_path.exists() or extract_path2.exists()):
            if (Path(tempfile.gettempdir()) / file_path.stem).exists():
                uf.remove(Path(tempfile.gettempdir()) / file_path.stem)
            if extract_path2.exists():
                ext_path = extract_path2
                flag = True
                break
            else:
                ext_path = extract_path
                flag = True
                break

    if flag:
        for file in ext_path.iterdir():
            if '.rsrc' in str(file):
                flag = False
                break
        if not flag:
            uf.remove(ext_path)
            ext_path = None

    return ext_path, flag


def extract_time_out():
    log.info("time out!")
    kill_all_process()
    batch = uniextract_path/"batch.queue"
    try:
        uf.remove(batch)
    except:
        log.error(f"no batch.queue file")


def kill_process(name):
    pids = psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
            process_name = p.name()
            if name in process_name:
                try:
                    import subprocess
                    subprocess.Popen(
                        "cmd.exe /k taskkill /F /T /PID %i" % pid, shell=True)
                except OSError:
                    log.error(f"kill process {process_name} failed")
        except:
            continue


def kill_all_process():
    for name in kill_name:
        kill_process(name)
