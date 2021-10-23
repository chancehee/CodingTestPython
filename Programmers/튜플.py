'''
프로그래머스(level2): <튜플>
'''

# 느낀점 정규표현식을 공부하면 더 간결하게 코드를 작성할 수 있다..
s = "{{20,111},{111}}"

s = s[2:-2]
a = s.split('},{')

a.sort(key=lambda x:len(x))
print(a)

arr = []
for i in a:
    b=i.split(',')
    for j in b:
        if j.isdigit() and j not in arr:
            arr.append(j)
print(arr)



