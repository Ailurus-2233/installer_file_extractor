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
# uniextract_path = Path('../python_env/python_shell/file_unpack/uniextract2')
uniextract_path = Path('./uniextract2')
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
# temp_path = Path('../upload/tmp_software/')
temp_path = Path('D:/Documents/项目开发/工控供应链项目/temp')


'''
文件名长度限制
'''
file_name_len = 100


'''
超时kill进程
'''

kill_name = ['7ZSplit.exe', 'acefile.exe', 'arc.exe', 'arc_conv.exe', 'arj.exe', 'AspackDie.exe',
             'bitrock-unpacker.exe', 'bootimg.exe', 'bsab.exe', 'Champollion.exe', 'ci-extractor.exe',
             'cicdec.exe', 'clit.exe', 'daa2iso.exe', 'dark.exe', 'demoleition.exe',
             'EnigmaVBUnpacker.exe', 'exeinfope.exe', 'file.exe', 'fsbext.exe', 'GARbro.Console.exe',
             'godotdec.exe', 'helpdeco.exe', 'i6comp.exe', 'innoextract.exe', 'innounp.exe',
             'IsXunpack.exe', 'jsMSIx.exe', 'kgb2_console.exe', 'lbrate.exe', 'lconvert.exe',
             'lessmsi.exe', 'lzip.exe', 'lzop.exe', 'msgunfmt.exe', 'MsiX.exe', 'mtee.exe',
             'NBHextract.exe', 'pdfdetach.exe', 'pdftohtml.exe', 'pdftopng.exe', 'pdftotext.exe',
             'pea.exe', 'PEiD.exe', 'quickbms.exe', 'RgssDecrypter.exe', 'rmvdec.exe', 'sfarkxtc.exe',
             'sgbdec.exe', 'simdec.exe', 'spoondec.exe', 'sqlite3.exe', 'swfextract.exe', 'trid.exe',
             'ttarchext.exe', 'uif2iso.exe', 'umodel.exe', 'unadf.exe', 'unalz.exe', 'unar.exe',
             'unarc.exe', 'unecm.exe', 'unisz.exe', 'unlzx.exe', 'unrpa.exe', 'unshield.exe',
             'unzip.exe', 'unzoo.exe', 'upx.exe', 'utagedec.exe', 'uudeview.exe', 'VIS3Ext.exe',
             'WUN.exe', 'bcm.exe', 'UnRAR.exe', 'zpaq.exe', '7z.exe', 'bcm.exe', 'UnRAR.exe',
             'zpaq.exe', 'xor.exe', 'UniExtract.exe']
