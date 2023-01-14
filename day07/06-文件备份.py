f = open('../day06/1.txt', 'r', encoding='utf-8')
buf = f.read()

f1 = open('a备份.txt', 'w', encoding='utf-8')
f1.write(buf)
f.close()
f1.close()