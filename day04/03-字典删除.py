my_dict = {'name': "Tom", 'age': 18, 'hobby': ["basketball", "swimming"]}
del my_dict['name']
print(my_dict)
my_dict.pop('age')
print(my_dict)
my_dict.clear()
print(my_dict)

del my_dict  # 直接删除字典，下面不能再使用，除非重新定义
print(my_dict)
