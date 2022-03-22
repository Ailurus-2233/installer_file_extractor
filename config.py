from pathlib import Path

'''
回调接口位置
'''
url = 'http://localhost:8080/unpack/callback'


'''
解压目标文件格式
'''
# ext_type_list = ['.001', '.7Z', '.BIN', '.BZ2', '.CAB', '.CPIO', '.EXE', '.GZ', '.IMG', '.IPK', '.ISO', '.JAR',
#                 '.LZ', '.MSI', '.MSM', '.MSP', '.MSU', '.TAR', '.TBZ2', '.TGZ', '.TXZ', '.TZ', '.ZIP', '.ZOO', '.RAR']
# ext_type_list += [x.lower() for x in ext_type_list]
# ext_type_list = list(set(ext_type_list))

ext_type_list = ['.001', '.7Z', '.7z', '.BIN', '.BZ2', '.CAB', '.CPIO', '.EXE', '.GZ', '.IMG', '.IPK', '.ISO', '.JAR', '.LZ', '.MSI', '.MSM', '.MSP', '.MSU', '.RAR', '.TAR', '.TBZ2', '.TGZ', '.TXZ', '.TZ',
                 '.ZIP', '.ZOO', '.bin', '.bz2', '.cab', '.cpio', '.exe', '.gz', '.img', '.ipk', '.iso', '.jar', '.lz', '.msi', '.msm', '.msp', '.msu', '.rar', '.tar', '.tbz2', '.tgz', '.txz', '.tz', '.zip', '.zoo']

ext_save_list = ['.exe', '.EXE', '.msi', '.MSI', '.bin', '.BIN']


'''
解压深度
'''
ext_deep = 3


'''
uniextract2 位置
'''
# uniextract_path = Path('C:/Users/supplychain/Documents/file_unpack/uniextract2')
uniextract_path = Path('./uniextract2')
uniextract = uniextract_path/'Uniextract.exe'


# '''
# cache 文件夹目录
# '''
# cache_path = Path('./cache')
# cache_path = Path('C:/Users/supplychain/Documents/file_unpack/cache')


'''
exe 解压文件大小
'''
exe_size = 100 * 1024 * 1024


'''
文件
'''
save_list = ['.exe', '.EXE', '.dll', '.DLL', '.lib', '.LIB', '.md', '.MD', '.msi', '.MSI',
             '.txt', '.TXT', '.json', '.JSON', '.csv', '.CSV', '.html', '.HTML', '.bin', '.BIN']


'''
最大文件深度
'''
max_deep = 12
