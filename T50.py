# 定义两个set集合
A = {-1, 0, 1, 3, 67}
B = {9, -1, 2, 89, 4}

# 计算并集
union = A | B
print("并集:", union)

# 计算交集
intersection = A & B
print("交集:", intersection)

# 计算差集（A-B）
difference = A - B
print("差集:", difference)

# 将股票信息定义为二维列表
data = [
    ['159601', 'A50', 0.808, -0.62, 20662.66, '中国A50互联互通', -0.75, 0.8072, 0.8072, '2023-03-14', 260, 0.60, 537139, 0.13,
     43.40, '华夏基金'],
    ['159602', '中国A50', 0.806, -0.74, 3222.18, '中国A50互联互通', -0.75, 0.8066, 0.8067, '2023-03-14', 200, 0.60, 198254,
     0.08, 15.98, '南方基金'],
    ['159603', '双创天弘', 0.932, 0.00, 271.98, '科创创业50', 0.11, 0.9315, 0.9316, '2023-03-14', 100, 0.60, 220507, 0.10,
     20.55, '天弘基金'],
    ['159606', '500成长', 0.855, -1.04, 1013.83, '500质量', -1.09, 0.8547, 0.8548, '2023-03-14', 100, 0.60, 68422, -0.02,
     5.85, '易方达'],
    ['159608', '稀有金属', 0.753, -0.40, 1233.17, 'CS稀金属', -0.59, 0.7519, 0.7564, '2023-03-13', 80, 0.60, 19601, 0.01, 1.48,
     '广发基金'],
    ['159610', '500增强', 0.819, -0.85, 2964.57, '中证500', -0.89, 0.8201, 0.8195, '2023-03-14', 100, 0.60, 69257, 0.00,
     5.67, '景顺长城']
]

# 添加一条信息
new_row = ['159603', '新基金', 1.234, 0.56, 7890.12, '新领域', 1.23, 1.2345, 1.2346, '2023-03-15', 100, 0.50, 123456, 0.01,
           12.34, '新基金公司']
data.append(new_row)
print('After adding new row:', data)

# 删除一条信息
del data[1]
print('After deleting row:', data)

# 修改一条信息，将第一个基金的现价更改为0.809
data[0][2] = 0.809
print('After modifying data:', data)


# 查找一条信息
# Function to search for a row of data
def search_data(data, keyword):
    for row in data:
        if keyword in row:
            return row
    return None


search_result = search_data(data, '新基金公司')
print('Search result:', search_result)

# 1定义一个字典，学号作为key， 学生信息作为value，可以快速找到指定学号的学生信息
students_dict = {1: [1, '张三', '女', '2001/1/1', '汉', '信息管理与信息系统'],
                 2: [2, '李四', '男', '2001/1/29', '汉', '信息管理与信息系统'],
                 3: [3, '王五', '女', '2001/1/3', '汉', '计算机'],
                 4: [4, '赵大', '男', '2001/1/14', '汉', '人工智能']}
# 2.输出该表的所有信息：
for s in students_dict:
    print(students_dict[s])

# 3.修改学号4的性别为女
stu_4 = students_dict[4]
if stu_4:
    stu_4[2] = '女'
    students_dict[4] = stu_4
else:
    print('未找到学号为4的学生信息')
# 4.添加一条信息
add_student = [5, '李丽', '女', '2002-05-21', '朝鲜族', '经济学']
students_dict[5] = add_student

print(students_dict)
