import requests
import yaml
import time


def read_yaml(yaml_name):
    with open(yaml_name, encoding='utf-8') as file:
        data_dicts = yaml.full_load(file)
        return data_dicts


def request_url():
    data = read_yaml("request.yml")
    print(data)
    url_list = data['url']
    for url in url_list:
        try:
            info = requests.get(url)  # 发送get请求
            if info.status_code == 200:
                print("响应状态码是：" + str(info.status_code))
                print("编码类型是" + str(info.apparent_encoding))
            else:
                print("访问失败！")
        except requests.exceptions.ConnectTimeout:
            return True
        # info.encoding = 'utf-8'  # 可以更改编码类型
        # print("内容是" + info.text)  # 输出服务器返回的源代码内容


if __name__ == '__main__':
    request_url()
