import yaml
class Handler_Yaml():

    def read_yaml(self, yamlName, section, optin):
        # 打开yaml文件
        with open(yamlName, encoding='utf-8') as file:
            # 加载yaml数据
            data_dicts = yaml.full_load(file)  # 返回是多层字典
            # date_dicts数据是：
            # {'LOGIN': {'url': 'http://39.106.41.11:8080/login/',
            # 'data': {'username': 'jike2021', 'password': 'get_md5("12345qwert")'}},
            # 'user': {'demoer': 'jike', 'age': 18, 'bl': 'true', 'f': 1.2}}
            # 从字典中获取数据
            data = data_dicts[section][optin]

            # data原本是什么类型的数据，就返回什么类型的数据
            return data


if __name__ == '__main__':
    data1 = Handler_Yaml().read_yaml("./demo.yml", "LOGIN", "url")
    data2 = Handler_Yaml().read_yaml("./demo.yml", "user", "age")
    data3 = Handler_Yaml().read_yaml("./demo.yml", "user", "f")
    data4 = Handler_Yaml().read_yaml("./demo.yml", "user", "bl")
    data5 = Handler_Yaml().read_yaml("./demo.yml", "user", "l")
    print(f'数据是：{data5}，数据类型是：{type(data5)}')