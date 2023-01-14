class Vaccinator:

    def __init__(self, idCard, name):
        self.idCard = idCard
        self.name = name
        self.vaccination = {}

    def __str__(self):
        return f"接种人：{self.name},身份证号：{self.idCard},接种信息:{self.vaccination}"


def vaccination():
    name = input("请输入接种人姓名：")
    idCard = input("请输入接种人身份证号：")
    firstDate = input("请输入第一针接种日期：")
    firstPlace = input("请输入第二针接种地点：")
    vaccinator = Vaccinator(idCard, name)
    vaccinator.vaccination[firstDate] = firstPlace
    print(vaccinator)

vaccination()