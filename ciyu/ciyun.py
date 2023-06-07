import jieba  # 导入结巴分词
import wordcloud  # 导入wc词云
from imageio import imread  # 导入特定形状，用户可以自定义其他图形，我这里导入了某人的照片，注意照片背景要为白色

mask = imread("bang.jpg")  # 读取png图片
f = open("./file.txt", "r", encoding="utf-8")  # 只读形式打开中文文件
t = f.read()  # 将这个文档读取并赋值给t
f.close()  # 将文档关闭
ls = jieba.lcut("网球运动的运动量和运动强度可随意调整，因人而宜。不论男女老少，通过这种快人心扉、令人陶醉的网球运动和竞赛，都可达到增进健康、增进体质，强壮身心的目的")  # 将这个文档t利用jieba分词分为列表ls
txt = " ".join(ls)  # 将列表ls转换为用空格字符串替代分割的长字符串，并赋值给txt
w = wordcloud.WordCloud(font_path="./gular.otf", mask=mask, width=1000, height=700,
                        background_color="white")  # 设置字体、mask图片形状、长宽、背景色为白色
w.generate(txt)  # 向词云对象w加载txt文档内容
w.to_file("baseball.png")  # 生成一个blog的文档
