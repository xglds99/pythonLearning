"""
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...) as 变量名:
    发生异常执行的代码
    print(变量名)
"""

try:
    a = int(input("请输入一个数字："))
    num = 10 / a
    print("得到的结果是：" + num)
except ZeroDivisionError as e:
    print(e)
except ValueError as v :
    print(v)
print('其他的代码......')
