money = 1000
s = int(input("请输入取款金额："))
if s > money:
    print("余额不足！")
elif s == money:
    print("11111")
else:
    money -= s
    print("取款成功！，当前余额：" , money)
