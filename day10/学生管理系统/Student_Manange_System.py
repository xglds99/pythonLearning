import Student


class StudentManageSystem(object):
    def __init__(self):
        self.stu_dict = {}

    @staticmethod
    def __show_menu():
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 修改学生信息')
        print('4. 查询单个学生信息')
        print('5. 查询所有的学生信息')
        print('6. 退出系统')

    def start(self):
        self.__load_info()
        while True:
            self.__show_menu()
            opt = input('请输入用来选择的操作编号:')
            if opt == '1':
                # print('1. 添加学生')
                self.__insert_student()
            elif opt == '2':
                # print('2. 删除学生')
                self.__remove_student()
            elif opt == '3':
                # print('3. 修改学生信息')
                self.__modify_student()
            elif opt == '4':
                # print('4. 查询单个学生信息')
                self.__search_student()
            elif opt == '5':
                # print('5. 查询所有的学生信息')
                self.__show_all_info()
            elif opt == '6':
                self.__save()
                print('欢迎下次使用本系统......')
                break
            else:
                print('输入有误,请再次输入')
                continue

            input('...... 回车键继续操作.......')

    def __insert_student(self):
        # 1首先使用input获取学生信息
        stu_id = input('请输入学生学号:')
        # 对学号进行判断，判断学号是否存在
        while stu_id in self.stu_dict:
            stu_id = input('学号已存在，请重新输入:')
        name = input('请输入学生姓名:')
        age = input('请输入学生年龄:')
        gender = input('请输入学生性别:')
        # 2 使用学生信息创建学生对象
        stu = Student.Student(stu_id, name, age, gender)
        self.stu_dict[stu_id] = stu

    def __remove_student(self):
        stu_id = input('请输入要删除的学生学号：')
        if stu_id in self.stu_dict:
            del self.stu_dict[stu_id]
            print('学生已删除！')
        else:
            print('学号不存在，无法删除！')

    def __modify_student(self):
        stu_id = input('请输入要修改的学生学号：')
        if stu_id in self.stu_dict:
            stu = self.stu_dict[stu_id]
            stu.age = input('请输入修改后的年龄：')
            print('信息修改完毕')
        else:
            print('学生信息不存在，无法修改!')

    def __search_student(self):
        stu_id = input('请输入要删除的学生学号：')
        if stu_id in self.stu_dict:
            stu = self.stu_dict[stu_id]
            print(stu)
        else:
            print("学生信息不存在！")

    def __show_all_info(self):
        for stu in self.stu_dict.values():
            print(stu)

    def __save(self):
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.stu_dict.values():
            f.write(str(stu) + '\n')
        f.close()

    def __load_info(self):
        try:
            f = open('student.txt', 'r', encoding='utf-8')
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()
                info_list = buf.split(',')
                # 创建对象
                stu = Student.Student(*info_list)
                stu_id = info_list[0]
                self.stu_dict[stu_id] = stu
            f.close()
        except Exception as e:
            print(e)
