# 普通的形参 缺省形参 不定长元组形参 不定长字典形参
def func1(a, b=1, *args):  # 语法上不会报错， 缺省参数不能使用默认值
    pass


func1(1, 2, 15, 15)


def func2(a, *args, b=3):
    print(f"a:{a}")
    print(f"args:{args}")
    print(f"b:{b}")


func2(1, 3, 4, 5, 54, 6)