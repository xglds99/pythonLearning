f = open('a.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf:
        print(buf, end="")
    else:
        break
