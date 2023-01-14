def get_age(num):
    """
    求第 num 个人的年龄，每相邻的两个人的年龄相差两岁，已知第一个人的年龄是18岁
    :param num:
    :return:
    """
    if num == 1:
        return 18
    age = get_age(num-1) + 2
    return age


age = get_age(5)
print(age)