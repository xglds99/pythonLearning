import pymysql
import yaml


class Handler_Yaml():

    def read_yaml(self, yaml_name):
        with open(yaml_name, encoding='utf-8') as file:
            data_dicts = yaml.full_load(file)
            return data_dicts


if __name__ == '__main__':
    data = Handler_Yaml().read_yaml('./demo3.yml')
    conn = pymysql.connect(host = data['host'], port= data['port'], user=data['user'], password=data['password'], db=data['db'], charset=data['charset'])
    cur = conn.cursor()
    sql = "select * from ucenter_member where id = '1'"
    cur.execute(sql)
    data1 = cur.fetchone()
    print(data1)

