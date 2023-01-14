class Dog:
    dogCount = 0
    '''
    类的定义，dogCount为实体类变量，该类的所有实例共享该变量
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dogCount += 1

    def get_name(self):
        print("名字是：" + self.name)

    def get_age(self):
        print("age是：" + str(self.age + 1))

    def get_DogCount(self):
        print("狗的总数是：" + str(Dog.dogCount))


dog = Dog("Tom", 20)
dog1 = Dog("Axis",22)
print(id(dog))
dog.get_name()
dog.get_age()
dog.get_DogCount()
