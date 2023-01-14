"""
匿名函数
匿名函数不需要显示地定义函数名，使用【lambda + 参数 +表达式】的方式，即：
 lambda [arg1 [,arg2, ... argN]] : expression
"""

#无参无返回值
var = lambda: print('Hello lambda')
var()


#有参有返回值
f3 = lambda name:print(name)
f3('hello')


#有参有返回值
f4 = lambda name:name+'1'
print(f4('2'))