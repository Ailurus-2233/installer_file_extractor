import utils.uniextract as uu
import utils.file as uf
from func_timeout import func_set_timeout, FunctionTimedOut

type_list = [".zip", ".ZIP", ".rar", ".RAR", ".gz", ".GZ", ".iso",
             ".ISO", ".cab", ".CAB", ".7z", ".7Z"]


@func_set_timeout(600)
def run_root_extract(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


@func_set_timeout(100)
def run_sub_extract(file_path, extract_path):
    uu.run_extract(file_path, extract_path)


def extract_root(file_path, extract_path):
    _, flag = uu.check_extract_path(file_path, extract_path)
    if not flag:
        uf.backup(file_path)
        try:
            run_root_extract(file_path, extract_path)
        except FunctionTimedOut:
            uu.extract_time_out()
        if not file_path.exists():
            uf.restore(file_path)
        uf.remove_file(str(file_path)+".bak")


def extract_sub(file_path, extract_path):
    _, flag = uu.check_extract_path(file_path, extract_path)
    if not flag:
        try:
            run_sub_extract(file_path, extract_path)
        except FunctionTimedOut:
            uu.extract_time_out()
        _, flag = uu.check_extract_path(file_path, extract_path)
        if flag and file_path.suffix in type_list:
            uf.remove_file(file_path)