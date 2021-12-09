'''
그리디 : <팰린드롬 만들기>
'''
from collections import Counter
name = input()

a =Counter(name)
b =list(a.items())

cnt = 0
for i in b:
    if i[1]%2==1:
        cnt += 1

name_list = list(name)
name_list.sort()

x = ""
y = ""

if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    temp = 0
    for i in b:
        if i[1]%2==1:
            temp = i[0]
    if temp == 0:
        for i in range(len(name_list)):
            if i%2==0:
                x = x+name_list[i]
            else:
                y = name_list[i] + y
    else:
        name_list.remove(temp)
        for i in range(len(name_list)):
            if i%2==0:
                x = x+name_list[i]
            else:
                y = name_list[i] + y
        x = x+temp

print(x+y)

