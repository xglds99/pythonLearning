class Potato:

    potato_count = 0

    def __init__(self, status, total_time):
        self.status = status
        self.total_time = total_time
        self.name_list = []
        Potato.potato_count += 1

    def cook(self, time):
        self.total_time += time
        if 0 <= self.total_time < 3:
            self.status = '生的'
        elif 3 <= self.total_time < 6:
            self.status = '半生不熟'
        elif 6 <= self.total_time < 8:
            self.status = '熟的'
        else:
            self.status = '糊了'

    def add(self, name):
        self.name_list.append(name)

    def __str__(self):
        buf_list = ','.join(self.name_list)
        return f"地瓜烤制时间{self.total_time},地瓜当前状态{self.status},当前调料:{buf_list}"

    def get_count(self):
        print(f"地瓜数量：{self.potato_count}")


potato = Potato('生的', 0)
potato1 = Potato('生的', 0)
potato.cook(5)
potato.add("孜然粉")
print(potato)
potato.cook(2)
potato.add("辣椒面")
print(potato)

print('*' * 30)
potato.get_count()
potato1.get_count()



