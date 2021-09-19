'''
프로그래머스(level1): <실패율>
'''

# 시간 초과  1 6 7 9 13 23 24 25
# 분모가 0인경우 예외 분류하여 성공 !!
fail = {}
N = 5
stages = [1,1,1,1,1]

b = len(stages)

for i in range(1,N+1):
    if b == 0: # ZeroDivisionError: division by zero
        a = stages.count(i)
        fail[i] = a/b
        b = b - a
    else:
        fail[i] = 0


result = sorted(fail, key= lambda x: fail[x], reverse=True)
print(result)



'''
# 다른 사람 풀이(1)
N = 5
stages = [2,1,2,6,2,4,3,3]
k = len(stages) # 8
s = []
for i in range(1,N+1):
    c = 0
    for j in range(len(stages)):
        if stages[j] == i:
            c = c + 1
    if c == 0:
        s.append(0)
    else:
        s.append(c/k)
    k = k - c

a = sorted(s,reverse=True)
print('a',a)
answer = []

print('s',s)
for i in range(len(s)):
    answer.append(s.index(a[i])+1)
    s[s.index(a[i])]=2
print(answer)
'''

'''
#다른 사람 풀이(2)
N = 5
stages = [2,1,2,6,2,4,3,3]
result = {}
d = len(stages)
for stage in range(1,N+1):
    if d != 0:  # 이거 한 줄이 중요 !!!!!
        count = stages.count(stage)
        result[stage] = count/d
        d = d - count
    else:
        result[stage] = 0
print(sorted(result, key=lambda x: result[x], reverse=True))
'''