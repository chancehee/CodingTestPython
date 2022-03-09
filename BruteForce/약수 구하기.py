'''
브루트포스: <약수 구하기>
'''

# n 의 약수 중에서 k 번째로 작은 수를 출력
n, k = map(int, input().split())


# 약수 구하는 함수
def get_divisor(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


divisor = get_divisor(n)
# 값이 있다면
if divisor and len(divisor) + 1 > k:
    print(divisor[k - 1])
else:
    print(0)
