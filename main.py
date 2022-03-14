import argparse
from pathlib import Path
import utils.file as uf
import utils.uniextract as uu
import utils.extract as ue
from tqdm import tqdm
import os
from utils.net import sent_info
from config import ext_deep, ext_save_list


def main(args):
    file_path = Path(args.file_path)
    extract_path = args.extract_path

    '''
    新建文件夹操作
    '''
    if args.new_folder:
        new_folder = file_path.parent/file_path.stem
        new_folder.mkdir(parents=True, exist_ok=True)
        uf.move(file_path, new_folder)
        file_path = new_folder/file_path.name
        extract_path = new_folder/file_path.stem

    '''
    解压安装包文件
    '''
    if extract_path == "/sub":
        extract_path = file_path.parent/file_path.stem
    ue.extract_root(file_path, extract_path)
    extract_path, flag = uu.check_extract_path(file_path, extract_path)

    '''
    深度解压子文件
    '''
    sub_exec_list = []
    if flag:
        height = 0
        while height < ext_deep:
            height += 1
            file_list = uf.get_file_list(extract_path)
            if file_list == []:
                break
            index = 0
            for file in tqdm(file_list):
                index += 1
                if file not in sub_exec_list:
                    extract_sub_path = file.parent/file.stem
                    if file.suffix in ext_save_list:
                        sub_exec_list.append(file)
                        ue.extract_sub(file, extract_sub_path)
                    else:
                        ue.extract_sub(file, extract_sub_path)
                percent = index / len(file_list) / ext_deep + height/ext_deep
                sent_info(args.task_id, percent, extract_path, 0)
            sent_info(args.task_id, height/ext_deep, extract_path, 0)
        sent_info(args.task_id, 1, extract_path, 1)
    else:
        # 发送请求解压失败:
        sent_info(args.task_id, 0, extract_path, -1)
        print("error")

    uf.remove_useless_file(extract_path)
    uf.remove_empty_folder(extract_path)

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--file_path", '-fp')
    parse.add_argument("--extract_path", "-ep", default="/sub")
    parse.add_argument("--task_id", "-ti")
    parse.add_argument("--new_folder", "-nf", default=False, type=bool)
    main(parse.parse_args())
