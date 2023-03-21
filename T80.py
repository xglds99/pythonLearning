import turtle
turtle.screensize(bg="black")#设置背景颜色
turtle.goto(100,100)

turtle.color("green")
turtle.begin_fill()
# 循环4次
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
turtle.done()



#2-3
x = float(input("x= "))
y = float(input("y= "))
t = x
x = y
y = t
print("x: %f" % x)
print("y: %f" % y)

#task 1
weight = int(input("请输入体重(千克): "))
ptime = float(input("请输入跑步时间(分钟): "))
speed = int(input("请输入跑步速度(千米/小时)"))
distance = ptime * speed
print("跑步距离: %f" % distance)
caloris = weight * ptime / 60 * 5.6
print("燃烧卡路里: %f" % caloris)

#task 2
year = int(input("请输入年龄: "))
print('你已经过了: {0} 天'.format(year * 365))
print('你已经过了: {0} 小时'.format( year * 365 * 24))
print('你已经过了: {0} 分钟'.format(year * 365 * 24 * 60))
print('你已经过了: {0} 秒'.format(year * 365 * 24 * 60 * 60))


school = str(input("请输入你的学校: "))
clazz = str(input("请输入你的班级: "))
name = str(input("请输入你的姓名: "))
goal = str(input("请输入你的短期目标: "))

print("学校:{0},班级:{1},姓名:{2},大学四年的短期目标：{3}".format(school, clazz, name, goal))

n = int(input("请输入一个整数:"))
ans = n * n * n
print("N的三次方: %d" % ans)


print("乐万家超时收银系统")
goods_name = input("商品名称: ")
price = float(input("商品单价: "))
nums = int(input("商品数量: "))
discount = float(input("商品折扣: "))
real_pay = price * nums * discount
print("应付: %f" % real_pay)
real_get = float(input("实收: "))

print("乐万家超时 购物小票")
print("商品名称\t 价格\t 数量\t 折扣")
print(goods_name + "\t\t" + str(price) + "\t\t" + str(nums) + "\t\t"  + str(discount))
print("应付: %.2f" % real_pay)
print("实收: %d" % real_get)
print("找零: %.2f" % (real_get - real_pay))

