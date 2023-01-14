import chardet

path = 'meal_order_detail.xlsx'
f = open(path, 'rb')
data = f.read()
print(chardet.detect(data))
