"""
类型的可变与不可变：在不改变变量的引用的前提下，能否改变变量中引用的数据
如果能改变是可变类型，如果不能改变，是不可变类型
int floor bool str list tuple dict
可变类型：list dict set
不可变类型： number：int floor str tuple
python基本数据类型
Number:int long float complex
String :str
List: 列表列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
Tuple ：Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
Set：集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
Dict：相当于java中的键值对，map，
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
"""
my_list = [10, 20, 30]
print(id(my_list))
my_list.append(15)
print(id(my_list))

my_tuple = (10, 20, 'a')
print(id(my_tuple))
my_tuple = (10, 20, 'b')
print(id(my_tuple))