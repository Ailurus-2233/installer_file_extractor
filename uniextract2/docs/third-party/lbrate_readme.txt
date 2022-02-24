This package contains the Windows build of the lbrate tool written by Russell Marks (http://www.svgalib.org/rus/lbrate.html).

This archive consists of the following folders/files:
* bin\lbrate.exe  - the compiled utility that can be run directly
* doc\lbrate.html - documentation for lbrate converted from a man page to a HTML file for easier viewing on Windows
* src\*           - unmodified contents of the original downloaded package


Build notes
***********
This executable was built by extracting the downloaded archive (see the author's web site) and compiling as-is without any modifications using the MinGW toolchain. It was then stripped from ~71K to ~43K by excluding symbol information and unneeded sections. It is a native 32-bit Windows binary with no dependencies other than msvcrt.dll, thus can be run under virtually any Windows version. The manual was converted using man2html.


Usage notes
***********
If you happen to have a library file starting with a hyphen ('-'), you have to put a double hyphen surrounded by a space from each side before the file name on the command line (like `lbrate [options] -- filename.lbr'). It is to tell the command line parser to stop processing options so that it won't regard the file name mistakenly as another option. This behaviour is not documented in the manual. Note that this is not a feature of this build, this stems from using the getopt function used to parse the command line.


Contact me
**********
If you wish to contact me for whatever reason, you can do so by writing an e-mail to peersoft@outlook.com. Although I have brought this utility to Windows, credits go mainly to its developer, Russell Marks, who made life of CP/M fans better. Thanks!
