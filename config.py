from pathlib import Path

'''
回调接口位置
'''
url = 'http://localhost:8080/unpack/callback'


'''
解压目标文件格式
'''
ext_type_list = ['.zip', '.ZIP', '.rar', '.RAR', '.gz', '.GZ', '.iso',
                 '.ISO', '.msi', '.MSI', '.exe', '.EXE', '.cab', '.CAB', '.7z', '.7Z']
ext_save_list = ['.exe', '.EXE', '.msi', '.MSI']
ext_delete_list = ['.zip', '.ZIP', '.rar', '.RAR', '.gz', '.GZ', '.iso',
                   '.ISO', '.cab', '.CAB', '.7z', '.7Z']


'''
解压深度
'''
ext_deep = 3


'''
uniextract2 位置
'''
# uniextract_path = Path(
    # 'C:/Users/supplychain/Documents/file_unpack/uniextract2')
uniextract_path = Path('./uniextract2')
uniextract = uniextract_path/'Uniextract.exe'


'''
cache 文件夹目录
'''
cache_path = Path('./cache')
# cache_path = Path('C:/Users/supplychain/Documents/file_unpack/cache')


'''
exe 解压文件大小
'''
exe_size = 100 * 1024 * 1024


'''
文件
'''
save_list = ['.exe', '.EXE', '.dll', '.DLL', '.lib', '.LIB', '.md', '.MD',
             '.txt', '.TXT', '.json', '.JSON', '.csv', '.CSV', '.html', '.HTML']
