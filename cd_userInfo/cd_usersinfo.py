import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 更改绘图风格
plt.style.use('ggplot')

# 导入数据
columns = ['user_id', 'order_dt', 'order_products', 'order_amount']
df = pd.read_table('CDNOW_master.txt', names=columns, sep='\s+')  # sep='\s+'匹配任意空格
print(df.describe())

# 日期格式需要转换
df['order_date'] = pd.to_datetime(df['order_dt'], format='%Y%m%d')
# format参数：按照指定的格式去匹配要转换的数据列
# %Y：1994  %m：两位月份  %d：两位天
# %y：两位年份94 %h：两位小时09 %M：两位分钟  %s：两位秒
df['mouth'] = df['order_date'].astype('datetime64[M]')

plt.figure(figsize=(20, 15))

# 每月的产品购买数量
plt.subplot(221)
df.groupby(by='mouth')['order_products'].sum().plot()
plt.title('每月的产品购买数量')

# 每月消费金额
plt.subplot(222)
df.groupby(by='mouth')['order_amount'].sum().plot()
plt.title('每月的产品营业额')

# 每月消费次数
plt.subplot(223)
df.groupby(by='mouth')['user_id'].count().plot()
plt.title('每月的消费次数')

# 每月消费人数
plt.subplot(224)
df.groupby(by='mouth')['user_id'].apply(lambda x: len(x.drop_duplicates())).plot()
plt.title('每月的消费人数')

plt.show()
