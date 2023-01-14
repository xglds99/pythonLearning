file_name = input('请输入要备份的文件名：')

f = open(file_name, 'rb')
buf = f.read()
f.close()

# 根据源文件名，找到文件后缀和文件名
index = file_name.rfind('.')
# 后缀 file_name [index:]
#新文件名
new_file_name = file_name[:index] + "[备份]" + file_name[index:]
f_w = open(new_file_name, 'wb')
f_w.write(buf)
f_w.close()