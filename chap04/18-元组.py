import requests

url = "http://localhost:8080/FirstHtml/FirstHtml.html"

# GET
# 参数：显示传递
# url = url + "?param1=123&param2=456"
# res = requests.get(url)
# res.encoding = "UTF-8"
# print(res.text)

#参数: 隐式传递
params = {
    "param1": "123",
    "param2": "456"
}
# res = requests.get(url, params=params)
# res.encoding = "urf-8"
# print(res.text)

# POST
url_post = "https://www.bilibili.com/post"
header = {
    "customHeader" : "i am header"
}
cookie = {
    "token" : "dawdawdawdawdadawd",
    "token1": "123123123"
}
s = requests.session()
s.keep_alive = False

res = requests.post(url_post, headers=header, params=params, cookies=cookie)
res.encoding = "utf-8"
print(res.text)
