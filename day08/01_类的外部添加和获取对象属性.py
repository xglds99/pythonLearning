def play():
    print("修狗快乐的柴家！！！")


class Dog:
    """
    在实例上面添加外部属性，每个对象有不同的属性，不同对象之间设置属性不会共享
    """


dog = Dog()
play()
dog.name = "Tom"
dog.age = 21
print(str(dog.age) + dog.name)

dog1 = Dog()

print(Dog.__dict__)
