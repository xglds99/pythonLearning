#1.
s = input("请输入一个字符串：")
count = s.count('a')
print(count)

input_str = input("输入一个带有py的字符串:")
output_str = input_str.replace("py", "python")
print(output_str)

num = 0x1010
hex_str = hex(num)   # 十六进制
dec_str = str(num)   # 十进制，直接转换为字符串
oct_str = oct(num)   # 八进制
bin_str = bin(num)   # 二进制

print(hex_str, dec_str, oct_str, bin_str, sep=',')

num = int(input("请输入一个正整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
