string_array = ["600718", "600039", "655384", "941859", "157479"]
count = 0
for my_str in string_array:
    print(my_str)
    my_list = list(my_str)
    print(my_list)
    for i in my_list:
        if 9 == int(i):
            count +=1

print(count)




