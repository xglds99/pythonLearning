import os
import datetime
# 1、重命名文件
# os.rename('a.txt', '1.txt')
# 2、删除文件
# # os.remove('a备份.txt')
#
# # 3、新建目录
# date= datetime.date
# print(date)
# os.mkdir(str(date))

# 4、删除空目录
# os.rmdir('../day08')

# 5 、获取当前所在的目录  get current working directory
# buf = os.getcwd()
# print(buf)


#  6 、修改当前的目录， os.chdir(目录名)
# os.chdir('test')
# buf = os.getcwd()
# print(buf)

# 7、获取指定目录下内容，Return a list containing the names of the files in the directory.
buf = os.listdir('../day07')
print(buf)