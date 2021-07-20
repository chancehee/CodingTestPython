# 소수를 구하기 위한 에라토스테네스의 체 (코딩테스트 시간 절약을 위한 학습)

# 시간 복잡도 O(Nlog(logN))
def prime_list(n):
    Net = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if Net[i] == True: #i가 소수인 경우
            for j in range(i+i, n, i):
                Net[j] = False
    return [i for i in range(2,n) if Net[i]==True]
result = prime_list(100)
print(result)

