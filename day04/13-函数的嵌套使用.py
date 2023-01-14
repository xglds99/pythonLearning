def func1():
    print("func1被调用！")


def func2():
    print("func2被调用了！")


def func3():
    func1()
    func2()
    print("func3被调用了！")


func3()