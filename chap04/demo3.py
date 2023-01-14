sum = 0
a = 1

while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1
print(sum)

for i in range(10):
    sum += i
print(sum)

for i in range(100, 1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)

lst = ['hello', 'world', 99]


