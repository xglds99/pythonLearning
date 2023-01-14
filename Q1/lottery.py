import random


def getNumList(start, end, n):
    """生成n个 [ start, end ] 区间内的不重复随机数"""  # 函数注释
    numsArray = set()
    while len(numsArray) < n:
        numsArray.add(random.randint(start, end))

    return list(numsArray)


def get_prize(numList):
    first_prize = 0  # 记录得奖的数量
    second_prize = 0
    third_prize = 0
    for num in numList:
        i = random.randint(1, 4)
        if i == 1 and first_prize < 5:
            first_prize += 1
            print(f"彩票：{num}获得一等奖！")
        elif i == 2 and second_prize < 10:
            second_prize += 1
            print(f"彩票：{num}获得二等奖！")
        elif i == 3 and third_prize < 50:
            third_prize += 1
            print(f"彩票：{num}获得三等奖！")
        else:
            print(f"彩票：{num}未中奖！")


numList = getNumList(1000, 9999, 500)
get_prize(numList)