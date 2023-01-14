"""
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
打开文件并返回一个流。
失败时引发 OSError。 file 是一个文本或字节字符串，给出要打开的文件的名称（如果文件不在当前工作目录中，则为路径）或要包装的文件的整数文件描述符。
（如果给定了文件描述符，则在关闭返回的 IO 对象时将其关闭，除非 closefd 设置为 False。）
 mode 是一个可选字符串，指定文件打开的模式。它默认为“r”，表示以文本模式打开以供阅读。
 其他常见的值是 'w' 用于写入（如果文件已经存在，则截断文件），
 'x' 用于创建和写入新文件，以及 'a' 用于附加（在某些 Unix 系统上，
 这意味着所有写入都附加到无论当前的查找位置如何，文件的结尾）。
 在文本模式下，如果未指定编码，则使用的编码取决于平台：调用 locale.getpreferredencoding(False) 以获取当前的语言环境编码。
"""
f = open('1.txt', 'r')
buf = f.read()
print(buf)
f.close()
