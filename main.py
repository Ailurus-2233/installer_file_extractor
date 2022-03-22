import argparse
from pathlib import Path

from sympy import E
import utils.file as uf
import utils.uniextract as uu
import utils.extract as ue
from rich.progress import track
from utils.net import sent_info
from config import ext_deep, ext_save_list
from utils.log import log


def main(args):
    file_path = Path(args.file_path)
    extract_path = args.extract_path

    '''
    新建文件夹操作
    '''
    if args.new_folder:
        new_folder = file_path.parent/file_path.stem
        log.info(f"Creating new folder:{new_folder}")
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
    log.info(f"Extract {file_path} to {extract_path}")

    '''
    深度解压子文件
    '''
    if flag:
        height = 0
        deleted_list = []
        while height < ext_deep:
            height += 1
            file_list, save_list = uf.get_file_list(extract_path)
            if file_list == []:
                sent_info(args.task_id, 1, extract_path, 1)
                break
            tmp_list = uf.load_cache_file(file_path)
            index = 0
            for file in track(file_list, description="[green]Extracting..."):
                log.info(f"extract file {file}")
                index += 1
                if file in tmp_list:
                    continue
                extract_sub_path = file.parent/file.stem
                tmp = ue.extract_sub(file, extract_sub_path)
                if tmp != None:
                    deleted_list.append(tmp)
                percent = index / len(file_list) / \
                    ext_deep + (height-1)/ext_deep
                sent_info(args.task_id, percent, extract_path, 0)
            sent_info(args.task_id, height/ext_deep, extract_path, 0)
            uf.add_cache_file(file_path, save_list)
        sent_info(args.task_id, 1, extract_path, 1)
    else:
        # 发送请求解压失败:
        sent_info(args.task_id, 0, extract_path, -1)
        log.error(f"Extract {file_path} failed")

    log.info("Save all files name to filenames.txt")
    uf.save_file_name(extract_path, deleted_list)

    log.info("Remove useless file")
    uf.remove_useless_file(extract_path)
    uf.remove_empty_folder(extract_path)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--file_path", '-fp')
    parse.add_argument("--extract_path", "-ep", default="/sub")
    parse.add_argument("--task_id", "-ti")
    parse.add_argument("--new_folder", "-nf", default=False, type=bool)
    main(parse.parse_args())
