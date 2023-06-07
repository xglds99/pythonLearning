import string

Str1 = "The pi equals to 3.1415926"
str1_list = Str1.split(' ')
print(str1_list)
print('Pi的值为: %.4f' % float(str1_list[4]))


##question2
Str2 ='AbCdEfG'
Str2_swap = ''
for char in Str2:
    if char.islower():
        Str2_swap += char.upper()
    elif char.isupper():
        Str2_swap += char.lower()
    else:
        Str2_swap += char
print(Str2_swap)


#2.2
Q1_answer = list(Str2_swap)
Q1_answer.extend(['1', '2', '!', r'\\'])
print(Q1_answer)


#2.3
Q2_answer_sorted = sorted(Q1_answer, reverse=True)
print(Q2_answer_sorted)
print(len(Q2_answer_sorted))


#2.4
backslash_index = Q1_answer.index(r'\\')
print(backslash_index)

#2.5
Q3_answer = [char for char in Q2_answer_sorted if not char.isupper()]
print(Q3_answer)
print(len(Q3_answer))


#2.6import string
Q5_answer = [char for char in Q3_answer if char not in string.punctuation]
print(Q5_answer)
print(len(Q5_answer))





