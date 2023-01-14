import \
    jieba  # 中文分词库 提供三种模式分词：精确  jieba.cut(s) 无冗余,全模式 jieba.lcut(s,cut_all =True) 有冗余, 探索模式 jieba.lcut_for_search(s) 有冗余
import collections  # 词频统计
import wordcloud # 生成词云
import matplotlib.pyplot as plt

with open('demo.txt', 'r', encoding='utf-8') as f:
    data = f.read()
w_cut = jieba.cut(data, cut_all=False)
word_list = []
word_remove = [u'，', u' ', u'。', u'、', u'\n', u'', u'的', u'是', u'了', u'我', u'我们', u'他']
for w in w_cut:
    if w not in word_remove:
        word_list.append(w)


word_counts = collections.Counter(word_list)
word_counts_top= word_counts.most_common(50)
print(word_counts_top)
print(type(word_counts_top))

word_cloud = wordcloud.WordCloud(
    font_path='simfang.ttf', #中文词频生成设置
    background_color = 'white',
    max_font_size =150
)
word_cloud.generate_from_frequencies(word_counts)
plt.figure(1, figsize=(10, 8))
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
word_cloud.to_file("wordclouddemo.png")