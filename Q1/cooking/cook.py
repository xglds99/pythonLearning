
import pandas as pd
import numpy as np

#1、加载数据
data1 = pd.read_excel('../data/meal_order_detail.xlsx',sheet_name='meal_order_detail1')
data2 = pd.read_excel('../data/meal_order_detail.xlsx',sheet_name='meal_order_detail2')
data3 = pd.read_excel('../data/meal_order_detail.xlsx',sheet_name='meal_order_detail3')

#2、数据预处理，（合并数据,NA处理，）分析数据
data = pd.concat([data1, data2, data3],axis=0)
print(data.info)
data.dropna(axis=1,inplace=True)
#3、统计卖出菜品的平均价格\n",
#print(round(data['amounts'].mean(),2))
#print(round(np.mean(data['amounts']),2)) #数据量大推荐

# 4、频数统计，什么菜最受欢迎  （对菜名进行频数统计，取最大前10名）\n",
dishes_count = data['dishes_name'].value_counts()[:10]
print(dishes_count)