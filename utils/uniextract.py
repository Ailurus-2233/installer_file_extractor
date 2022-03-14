import utils.file as uf
from pathlib import Path
import os
import tempfile
import time
import psutil
from config import uniextract, uniextract_path


def add_batch_queue(file_path, extract_path):
    if extract_path != "/sub":
        info = f'"{file_path}" "{extract_path}" /silent\n'
    else:
        info = f'"{file_path}" /sub /silent\n'
    uf.append(info, uniextract_path/"batch.queue")


def run_extract(file_path, extract_path):
    kill_process("UniExtract.exe")
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
    while temp_path.exists() or (extract_path.exists() or extract_path2.exists()):
        if not (extract_path.exists() or extract_path2.exists()):
            time.sleep(1)
        if (not temp_path.exists()) and (extract_path.exists() or extract_path2.exists()):
            if (Path(tempfile.gettempdir()) / file_path.stem).exists():
                uf.remove(Path(tempfile.gettempdir()) / file_path.stem)
            if extract_path2.exists():
                return extract_path2, True
            return extract_path, True
    return None, False


def extract_time_out():
    try:
        kill_process("IsXunpack.exe")
    except:
        print(f'[error]:没有名字为IsXunpack.exe进程')
    batch = uniextract_path/"batch.queue"
    try:
        uf.remove(batch)
    except:
        print(f'[error]:没有等待解压队列文件')


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
                    print(f'[error]:没有名字为{name}进程')
        except:
            continue
