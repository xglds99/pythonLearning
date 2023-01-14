def func(a, b):
    c = a + b
    d = a - b
    # return c, d 默认元组返回
    return {0: c, 1: d}  #字典返回


resu = func(1, 2)
print(resu[0], resu[1])
