# 组包，将多个数据值，组成元组，给一个变量

a = 1, 2, 3
print(a)

"""
拆包：
    将容器中的数据分别给到多个变量，需要注意，数据的个数和变量的个数要保持一致
"""

b, c, d = a
print(b, c, d)


def func():
    return 1, 2


e, f = func()
print(e, f)

my_list = [10, 20]

my_dict = {'name': 'Tom', 'age': 15}
a, b = my_dict
print(my_dict.get(a), my_dict.get(b))
