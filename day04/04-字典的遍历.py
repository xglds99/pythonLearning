my_dict = {'name': "Tom", 'age': 18, 'gender': '男', 'hobby': ["basketball", "swimming"]}
for key in my_dict:
    print(my_dict.get(key))

result = my_dict.keys()


print(result, type(result))
for key in result:
    print(key)


values = my_dict.values()
print(values, type(values))
for item in values:
    print(item)


print("***************"*12)
items = my_dict.items()
for item in items:
    print(item)

for k, v in items:
    print(k, v)
