import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud

# 获取微博热搜页面
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
response = requests.get(url)

# 解析页面
soup = BeautifulSoup(response.text, 'html.parser')
hot_list = soup.select('.td-02')

# 获取热搜词列表
words = []
for hot in hot_list:
    words.append(hot.text)
print(words)
# 分词
text = ' '.join(jieba.cut(' '.join(words)))

# 生成词云
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

# 保存词云图片
wordcloud.to_file('weibo_hot.png')