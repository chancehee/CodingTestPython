'''
프로그래머스(level2): <뉴스 클러스터링>
'''
# 풀었으나 2시간 정도 걸림.. 구현하는 시간을 줄이는 연습 필요
str1 = 'frfr'
str2 = 'frfr'

str1=str1.lower()
str2=str2.lower()

from collections import deque

queue1 = deque()
for i in range(len(str1)-1):
    if str1[i].isalpha() and str1[i+1].isalpha():
        queue1.append(str1[i]+str1[i+1])

queue2 = deque()
for i in range(len(str2)-1):
    if str2[i].isalpha() and str2[i+1].isalpha():
        queue2.append(str2[i]+str2[i+1])


#중복 X 리스트:  ex_list
ex1 = set(queue1)
ex2 = set(queue2)
ex_list = list(ex1 | ex2)

ex_set1 = {}
for i in ex_list:
    ex_set1[i] = 0
for i in ex_list:
    try:
        ex_set1[i] = queue1.count(i)
    except:
        pass

ex_set2 = {}
for i in ex_list:
    ex_set2[i] = 0
for i in ex_list:
    try:
        ex_set2[i] = queue2.count(i)
    except:
        pass


go = 0
hap = 0
for i in ex_list:
    hap = hap + max(ex_set1[i],ex_set2[i])
    go = go + min(ex_set1[i],ex_set2[i])


if go==0 and hap==0:
    result = 65536
else:
    result = int((go/hap) * 65536)
print(result)
