# 打开一个文件 ，文件不存在，则创建文件，文件存在，则会覆盖文件原来的内容
f = open('1.txt', 'w', encoding='utf-8')
"""
1、open函数打开文件，没有指定文件的编码，windows默认使用GBK编码
2、write函数在写入中文的时候，使用GBK编码写入
3、pycharm中打开文件，默认使用utf-8编码
4、使用utf-8编码打开gbk编码的文件，会出现乱码
 
编码：就是如何将中文汉字变为二进制，或者如何将二进制变为中文汉字
"""
# 写文件，文件对象.write('写入的内容')
f.write('hello,atguigu\n')
f.write('hello,中国\n')
# 3、关闭文件流
f.close()
