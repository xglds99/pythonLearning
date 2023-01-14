# 函数传参传递的也是引用

my_list = [1, 2, 3]


def func1(a):
    a.append(4)


def func2():
    my_list.append(5)


func2()
print(my_list)

func1(my_list)
print(my_list)
