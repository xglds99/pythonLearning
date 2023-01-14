my_dict = {'name': '电脑', 'price': 10000}


def num(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


num(name="电脑", price=700)
