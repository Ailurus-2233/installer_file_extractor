from pathlib import Path

'''
回调接口位置
'''
url = 'http://localhost:8080/unpack/callback'


'''
解压深度
'''
ext_deep = 3


'''
uniextract2 位置
'''
uniextract_path = Path('C:/Users/supplychain/Documents/file_unpack/uniextract2')
uniextract = uniextract_path/'Uniextract.exe'


'''
exe 解压最小文件大小
'''
exe_size = 50 * 1024 * 1024


'''
文件
'''
save_list = ['.exe', '.EXE', '.dll', '.DLL', '.lib', '.LIB', '.md', '.MD', '.msi', '.MSI',
             '.txt', '.TXT', '.json', '.JSON', '.csv', '.CSV', '.html', '.HTML', '.bin', '.BIN']


'''
文件分类
'''
file_type = {
    'bin': ['.exe', '.EXE', '.bin', '.BIN', '.dll', '.DLL', '.so', '.SO', '.lib', '.LIB'],
    'txt': ['.txt', '.TXT', '.json', '.JSON', '.csv', '.CSV', '.html', '.HTML', '.md', '.MD', '.xml', '.XML'],
    'ext': ['.001', '.7Z', '.7z', '.BZ2', '.CAB', '.CPIO', '.GZ', '.IMG', '.IPK', '.ISO',
            '.LZ', '.MSI', '.MSM', '.MSP', '.MSU', '.RAR', '.TAR', '.TBZ2', '.TGZ', '.TXZ',
            '.TZ', '.ZIP', '.bz2', '.cab', '.cpio', '.gz', '.img', '.ipk', '.iso', '.lz',
            '.msi', '.msm', '.msp', '.msu', '.rar', '.tar', '.tbz2', '.tgz', '.txz', '.tz', 
            '.zip']
}


'''
解压文件临时目录
'''
temp_path = Path('C:/tmp/software')

