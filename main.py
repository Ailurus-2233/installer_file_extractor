import argparse
from itertools import count
from pathlib import Path
import utils.file as uf
import utils.uniextract as uu
from tqdm import tqdm
import requests
import json
import time
from func_timeout import func_set_timeout, FunctionTimedOut


@func_set_timeout(50)
def run_sub_extract(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(300)
def run_root_extract(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


def sent_info(task_id, percent, extract_path, status):
    url = "http://localhost:8080/unpack/callback"
    data = {
        'taskId': task_id,
        'unpackDirName': str(extract_path),
        'status': status,
        'percent': int(percent*100)
    }
    print(f"[log]: post {data}")
    try:
        requests.post(url, json.dumps(data), headers=(
            {"content-type": "application/json"}))
    except:
        print(f'[error]: {url} 连接异常')


def main(args):
    file_path = Path(args.file_path)
    extract_path = args.extract_path
    if args.new_folder:
        # TODO 新建文件夹
        new_folder = file_path.parent/file_path.stem
        new_folder.mkdir(parents=True, exist_ok=True)
        uf.move(file_path, new_folder)
        file_path = new_folder/file_path.name
        extract_path = new_folder/file_path.stem
    # 检查是否解压过
    if extract_path == "/sub":
        extract_path1 = file_path.parent/file_path.stem
        extract_path2 = Path(str(extract_path)+"_已解包")
    if not (extract_path1.exists() or extract_path2.exists()):
        print("[log]: unpack root file")
        try:
            uf.backup(file_path)
            run_root_extract(file_path, extract_path)
        except FunctionTimedOut:
            print(f"[error]: {file_path} extract timeout")
            uu.extract_time_out()
        except:
            print(f"[error]: {file_path} extract error")
        if not file_path.exists():
            uf.restore(file_path)
        uf.remove_file(str(file_path)+".bak")
        if extract_path == "/sub":
            extract_path = file_path.parent/file_path.stem
        extract_path, flag = uu.check_extract_path(file_path, extract_path)
        if flag:
            # TODO 获取文件夹下的可解压文件列表
            type_list = [".zip", ".ZIP", ".rar", ".RAR", ".gz", "GZ" ".iso",
                         ".ISO", ".msi", ".MSI", ".exe", ".EXE", ".cab", ".CAB"]
            file_list = []

            def get_file_list(path: Path):
                for f in path.iterdir():
                    if (path / f.name).is_dir():
                        get_file_list(path / f.name)
                    if (path / f.name).is_file():
                        if (path / f.name).suffix in type_list:
                            file_list.append(path / f.name)
            get_file_list(extract_path)
            count = 0
            page = len(file_list)//5 + 1
            for file in tqdm(file_list):
                count += 1
                if count % page == 0:
                    sent_info(args.task_id, count /
                              (len(file_list)+1), extract_path, 0)
                try:
                    run_sub_extract(file, "/sub")
                except FunctionTimedOut:
                    print(f"[error]: {file} extract timeout")
                    uu.extract_time_out()
                except Exception:
                    print(f"[error]: {file} extract error")
            sent_info(args.task_id, 1, extract_path, 1)
        else:
            # 发送请求解压失败
            sent_info(args.task_id, 0, extract_path, -1)
    else:
        # 发送请求已解压
        print("[log]: The file has been unpacked")
        if extract_path1.exists():
            extract_path = extract_path1
        else:
            extract_path = extract_path2
        sent_info(args.task_id, 1, extract_path, 1)

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--file_path", '-fp')
    parse.add_argument("--extract_path", "-ep", default="/sub")
    parse.add_argument("--task_id", "-ti")
    parse.add_argument("--new_folder", "-nf", default=False, type=bool)
    main(parse.parse_args())
