'''
프로그래머스(level2) : <이진 변환 반복하기>
'''

x = "1111111"

cnt = 0
i = 0
while (x != '1'):
    i = i + 1
    cnt = cnt + x.count('0')
    x = x.replace('0',"")
    print(len(x))
    x = bin(len(x))[2:]


print([i,cnt])
