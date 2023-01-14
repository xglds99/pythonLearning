import random

# 定义一个列表用来保存3个办公室
offices = [[], [], []]

# 定义一个列表用来存储8位老师的名字
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
a=0
for name in names:
    index = random.randint(0, 2)
    while len(offices[index]) >= 4:
        index = random.randint(0, 2)
    offices[index].append(name)
i = 1
for temp_names in offices:
    print('办公室%d的人数为:%d' % (i, len(temp_names)))
    i += 1
    for name in temp_names:
        print("%s" % name, end='')
    print("\n")
    print("-" * 20)

offices.index()