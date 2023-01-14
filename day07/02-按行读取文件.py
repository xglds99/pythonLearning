f = open('a.txt', 'r', encoding='utf-8')
buf = f.readline()
print(buf)
f.close()

s = open('a.txt', 'r', encoding='utf-8')
buff = s.readlines()
print(buff)
for a in buff:
    a = a.strip()
    b = a.split(',')
    print(a)
    print(b)

