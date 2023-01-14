# 全局变量 定义在函数外部的变量

g_num = 100


# 能否在函数内部修改全局变量的值  ==> 不能,这是在函数内部定义一个局部变量

def func():
    global g_num
    g_num = 2
    return g_num


print(func())
