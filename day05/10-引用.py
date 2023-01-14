"""
可以使用id()查看变量的引用，可以将id值认为是内存地址的别名
python中数据值的传递时引用
赋值运算符可以改变变量的引用
"""

# 将数据10 存储到变量a中，本质是将数据10所在内存的引用地址保存到变量a中
a = 10
print(id(a))
print(id(10))


my_list = [10, 20]
my_list2 = my_list
my_list.append(15)
my_list1 = my_list+[100, 200]
print(my_list1, my_list2)
print(id(my_list), id(my_list2))