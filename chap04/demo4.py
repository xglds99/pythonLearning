lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("源列表：", id(lst))

print(lst[1:6])

my_str3 = lst[1:5]
print(my_str3)

my_str = "hello world ha ha"
lst1 = my_str.split(" ")
print(lst1)
print(my_str)
print("*********")
my_str2 = my_str.replace("ha", "world",1)
print(my_str2)
for i in lst1:
    print(i)

