'''
수학: <소수 찾기>
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
#에라토스테네스의 체 참고(2의배수를 모두 지운다 -> 3의배수를 모두 지운다 -> ...
#소수 배열 구한 후 입력받은 배열이 소수배열에 있다면 카운트 증가

N = int(input())
num = list(map(int,input().split()))

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i, n , i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True ]

cnt = 0
arr = prime_list(1000)
for i in num:
    if i in arr:
        cnt = cnt+1
print(cnt)

