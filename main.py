import argparse
from pathlib import Path
import utils.file as uf
import utils.uniextract as uu
import utils.extract as ue
from tqdm import tqdm
from utils.net import sent_info
from config import exe_size, ext_deep
from utils.log import log
import os
import traceback


def extract_file(task_id, file_path, extract_path, test_flag, ex_deep=ext_deep):
    '''
    解压安装包文件
    '''
    if extract_path == "/sub":
        extract_path = file_path.parent/file_path.stem
    log.info(f"Extracting {file_path} to {extract_path}")
    ue.extract_root(file_path, extract_path)

    '''
    判断解压是否完成
    '''
    extract_path, flag = uu.check_extract_path(file_path, extract_path)

    if flag:
        '''
        按文件类型分类
        '''
        log.info(f"Classifying extract_path {extract_path}")
        uf.classify_file(extract_path)

        '''
        多层解压文件
        '''
        extract_history_list = uf.load_cache_file(extract_path)
        continue_type = ['.dll', '.DLL', '.lib', '.LIB', '.so', '.SO']
        for deep in range(ex_deep):
            bin_list = uf.get_type_file_list(extract_path, "bin")
            ext_list = uf.get_type_file_list(extract_path, "ext")
            file_list = bin_list + ext_list
            count = 0
            for file in tqdm(file_list, desc=f"Extracting level {deep+1}"):
                count += 1
                if file in extract_history_list or file.suffix in continue_type:
                    sent_info(task_id, deep/ext_deep + count /
                              len(file_list)/3, extract_path, 0, test_flag)
                    continue
                if file.suffix in ['.exe', '.EXE'] and os.stat(file).st_size < exe_size:
                    continue
                ue.extract_sub_temp(file, extract_path)
                extract_history_list.append(file)
                sent_info(task_id, deep/ext_deep + count /
                          len(file_list)/3, extract_path, 0, test_flag)
                uf.save_cache_file(extract_path, extract_history_list)
        sent_info(task_id, 1, extract_path, 1, test_flag)

        file_name = uf.get_all_file_list(extract_path)
        uf.save_file_name(extract_path, file_name)

        uf.remove_useless_file(extract_path)
    else:
        # 发送请求解压失败:
        sent_info(task_id, 0, extract_path, -1, test_flag)
        log.error(f"Extract {file_path} failed")


def extract_folder(folder_path: Path):
    for file in folder_path.iterdir():
        if file.is_dir():
            continue
        else:
            new_dir = file.parent/file.stem
            new_dir.mkdir(parents=True, exist_ok=True)
            uf.move(file, new_dir/file.name)
            extract_file(-1, new_dir/file.name, "/sub", True, ex_deep=2)


def main(args):
    file_path = Path(args.file_path)
    extract_path = args.extract_path
    test_flag = args.test_flag
    task_id = args.task_id
    if not args.folder:
        extract_file(task_id, file_path, extract_path, test_flag)
    else:
        extract_folder(file_path)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--file_path", '-fp')
    parse.add_argument("--extract_path", "-ep", default="/sub")
    parse.add_argument("--task_id", "-ti", default=-1)
    parse.add_argument("--test_flag", "-tf", default=False)
    parse.add_argument("--folder", "-f", default=False)
    args = parse.parse_args()
    try:
        main(args)
    except Exception as e:
        sent_info(args.task_id, 0, "", -1)
        exstr = traceback.format_exc()
        log.error(exstr)
