'''
수학: <베르트랑 공준>
'''

# 에라토스테스 체: 소수 구하기

def eratos(n):
    data = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if data[i] == True:
            for j in range(i+i, n+1, i):
                data[j] = False

    return [i for i in range(2,n+1) if data[i] == True ]


while True:
    n = int(input())
    if n==0:
        break

    a = eratos(2*n)
    cnt = 0
    for i in a:
        if i>n:
            cnt += 1

    print(cnt)



