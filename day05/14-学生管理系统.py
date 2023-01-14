import os
def showMenu():
    print('1. 添加学生')
    print('2. 删除学生')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


stu_list = []


def add_student():
    name = input('请输入学生姓名:')
    # [{},{},{}] 判断字典中的value是否存在
    for stu in stu_list:
        if stu["name"] == name:
            print('学生信息已存在')
            return
    age = input("请输入学生年龄:")
    gender = input('请输入学生性别:')
    stu_dict = {'name': name, 'age': age, 'gender': gender}
    stu_list.append(stu_dict)
    print('===============学生信息添加成功！==============')


def delete_student(name):
    for stu in stu_list:
        if stu['name'] == name:
            stu_list.remove(stu)
            break
    else:
        print('用户信息不存在')


def update_student(name):
    for stu in stu_list:
        if stu['name'] == name:
            stu['age'] = input('请输入新的年龄:')
            break
    else:
        print('用户信息不存在')


def search_student(name):
    for stu in stu_list:
        if stu['name'] == name:
            print(stu)
            break
    else:
        print('用户信息不存在')


def show_all_info():
    if len(stu_list):
        for item in stu_list:
            print(item)


def save():
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()


def load_file():
    global stu_list
    if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


def main():
    while True:
        showMenu()
        opt = input('请输入要选择的操作:')
        if opt == '1':
            add_student()
        elif opt == '2':
            name = input('请输入学生姓名')
            delete_student(name)
        elif opt == '3':
            name = input('请输入学生姓名')
            update_student(name)
        elif opt == '4':
            name = input('请输入学生姓名')
            search_student(name)
        elif opt == '5':
            show_all_info()
        elif opt == '6':
            print('欢迎下次使用本系统......')
            save()
            break
        else:
            print('输入有误,请再次输入')
            continue

        input('...... 回车键继续操作.......')


main()
