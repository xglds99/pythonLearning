import yaml


class ReadYaml(object):
    def __init__(self):
        self.file_name = 'demo1.yml'
        self.encoding = 'utf-8'

    def read_conf(self):
        # 首先将yaml文件打开，以file对象赋值给conf
        conf = open(file=self.file_name, mode='r', encoding=self.encoding)
        # 然后将这个file对象进行读取
        str_conf = conf.read()
        # 这里使用yaml.Load方法将读取的结果传入进去
        dict_conf = yaml.load(stream=str_conf, Loader=yaml.FullLoader)
        # 返回数据
        return dict_conf


if __name__ == '__main__':
    res = ReadYaml()
    driver = res.read_conf()['driver']['driver']
    print(driver)
