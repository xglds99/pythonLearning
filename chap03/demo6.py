flag = True

while flag:
    print("1:查询成绩等级")
    print("2:退出系统")
    action = int(input("请输入你的操作："))
    if action == 1:
        score = int(input("请输入成绩："))
        if score >= 90:
            print("成绩优秀！")
        elif 80 <= score < 90:
            print("成绩合格")
        elif 60 <= score < 80:
            print("成绩及格")
        else:
            print("成绩不在正确范围内！")
    else:
        flag = False
