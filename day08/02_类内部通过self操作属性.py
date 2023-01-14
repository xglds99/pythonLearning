class Dog:
    """
    self作为方法的第一个形参，再通过对象调用方法时，不需要手动传递值，是python解释器
    自动将调用该方法的对象传递给self，所以self这个形参代表的是对象
    """

    def __init__(self, name, age):
        self.hobby = None
        self.name = name
        self.age = age


dog = Dog(name="啃骨头")
print(f'小狗的爱好是' + dog.hobby)
