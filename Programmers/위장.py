'''
프로그래머스(level2): <위장>
'''


from collections import deque
# 옷 종류에 따른 조합법 공식에 따라 풀이

clothes = [['A','1'],['B','1'],['C','1'],['AA','2'],['BB','2']]

clothes.sort(key=lambda x:x[1])
print(clothes)

arr = []

cnt = deque()

for i in range(len(clothes)):
    if clothes[i][1] not in arr:
        cnt.append(i)
        arr.append(clothes[i][1])
cnt.append(len(clothes))


result = 1
while len(cnt)>1:
    b = cnt.popleft()
    a = cnt[0]
    result = result * (a-b+1)
if len(clothes)==1:
    print(1)
else:
    print(result-1)