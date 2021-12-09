import subprocess
import os
is_win = os.name == 'nt'

if is_win:
    charset = 'gbk'
    newline_symbol = '\r\n'
else:
    charset = 'utf-8'
    newline_symbol = '\n'


# 执行terminal指令并返回结果
def shell_res(shell):
    res = ""
    p = subprocess.Popen(
        shell, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    for line in p.stdout.readlines():
        try:
            info = line.decode(charset)
            if info != newline_symbol:
                res += info
        except:
            print(shell, "====", line)
    retvel = p.wait()
    return res, retvel


# 使用innounp解压文件
def extract_file_inno(file_path, extract_path=''):
    if extract_path == '':
        extract_path = f'{file_path}.extracted'
    cmd = f'innounp -x "{file_path}" -d"{extract_path}"'
    res, _ = shell_res(cmd)
    if "The setup files are corrupted or made by incompatible version. Maybe it's not an Inno Setup installation at all." in res:
        return None, False
    else:
        return res, True


# 判断文件是否可以用7z解压
def is_archive(file_path):
    cmd = f'7z l "{file_path}"'
    res, flag = shell_res(cmd)
    return not "Errors: 1" in res


# 使用7z解压文件
def extract_file_7z(file_path, extract_path=''):
    if extract_path == '':
        extract_path = f'{file_path}.extracted'
    cmd = f'7z x "{file_path}" -o"{extract_path}" -aoa'
    res, _ = shell_res(cmd)
    return not 'ERROR' in res.split(newline_symbol)[4], extract_path


skip_folders = ["resources", "node_modules"]
stop_folders = [".rsrc"]


# 7z递归的解压文件
def extract_file_recursion(file_path, extract_path="", deepth=0):
    if deepth > 10:
        return 0
    if os.path.isdir(file_path):
        ch_files = os.listdir(file_path)
        for ch_file in ch_files:
            if ch_file in skip_folders:
                continue
            if ch_file in stop_folders:
                return
            extract_file_recursion(file_path + "/" + ch_file)
    else:
        if is_archive(file_path):
            flag, extract_path = extract_file_7z(file_path, extract_path)
            ch_files = os.listdir(extract_path)
            for ch_file in ch_files:
                if ch_file in skip_folders:
                    continue
                if ch_file in stop_folders:
                    return
                extract_file_recursion(
                    extract_path + "/" + ch_file, deepth=deepth+1)
