def my_calc(a, b, func):
    num = func(a, b)
    print(num)


"""
匿名函数作为形参
"""


my_calc(10, 20, lambda a, b: a + b)
my_calc(10, 20, lambda a, b: a + b**2)