from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure(figsize=(10, 8))

n = 10
X = np.arange(n) + 1
Y1 = [38312224, 27462297, 24706321, 35712111, 43746323, 25575254, 57237740, 65683722, 59500510, 45966239]
Y2 = [31850088, 24707345, 24049155, 34915616, 42591407, 25019831, 57752557, 66444864, 61027171, 47209277]
plt.bar(X, Y1, width=0.2, facecolor='lightskyblue', edgecolor='white')
plt.bar(X+0.2, Y2, width=0.2, facecolor='yellowgreen', edgecolor='white')
# 给图加text
for x, y in zip(X, Y1):
    plt.text(x - 0.1, y, '%d' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x + 0.15, y + 0.001, '%d' % y, ha='center', va='bottom')

names = ['', '黑龙江', '吉林', '内蒙古', '山西', '辽宁', '甘肃', '湖北', '湖南', '安徽', '云南']
x = range(len(names))
plt.xticks(x, names, rotation=10)
plt.margins(0.1)
plt.legend(('第六次人口普查', '第七次人口普查'))
plt.xlabel(u"省份")  # X轴标签
plt.ylabel("人口数量")  # Y轴标签
plt.title(u"第六次人口普查与第七次人口普查省份人口数量变化")  # 标题
plt.ylim(0, 70000000)
plt.show()
fig.savefig('pic.jpg')