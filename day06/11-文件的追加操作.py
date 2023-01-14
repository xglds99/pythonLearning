"""
a 方式打开文件，追加内容
"""
f = open('a.txt', 'a', encoding='utf-8')
f.write('你好，山东')
f.close()
