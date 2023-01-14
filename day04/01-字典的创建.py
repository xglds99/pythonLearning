"""
字典 dict使用{}定义，是由键值对组成
"""
my_dict = {}
my_dict1 = dict()
print(my_dict, type(my_dict))
my_dict2 = {'name': 'Tom', 'age': 15, 'hobby': ['basketball', 'pingpang', 'football'], 1: [2, 5, 8]}
print(my_dict2['age'])
print(my_dict2['hobby'][1])
print(my_dict2.get('gender', 1))
