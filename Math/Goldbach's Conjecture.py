'''
수학: <골드바흐의 추측>
문제
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
이 추측은 아직도 해결되지 않은 문제이다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.
 테스트 케이스의 개수는 100,000개를 넘지 않는다.
각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다.
숫자와 연산자는 공백 하나로 구분되어져 있다.
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.
'''

#아이디어
'''
입력받은수에 가장 작은 소수를 뺀다 그 숫자가 소수이면 성립
소수가 아니라면 가장 작은 소수를 크기를 키워가면 빼기 최종 소수 + 소수 인지
아니라면 예외
시간 초과 -> 어떻게 해결 할까?

'''

#1차시도 -> 시간초과
'''
def p_number(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False

    return True

while True:
    a=0
    b=0
    N = int(input())
    if N ==0:
        break

    int_list = (i for i in range(2, N+1))
    p_numbers = []
    for i in int_list:
        if p_number(i):
            p_numbers.append(i)

    p_numbers.remove(2)


    for i in range(len(p_numbers)):
        if (N - p_numbers[i]) in p_numbers:
            a = p_numbers[i]
            b = N-p_numbers[i]
            break
        else:
            pass

    if a==0 and b==0:
        print("Goldbach's conjecture is wrong." )
    else:
        print(str(N) + ' = '+str(a)+ ' + '+str(b))
'''

#2차시도 시간초과  입력값을 readline으로 받았더니 시간초과에러 해결
#또한 에라토스테네스의 체를 이용하여 미리 100만까지 소수 리스트를 구한후 진행함.
import sys
input = sys.stdin.readline
def prime_list(n):
    Net = [True] * n
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if Net[i] == True: #i가 소수인 경우
            for j in range(i+i, n, i):
                Net[j] = False

    return [[i for i in range(2,n) if Net[i]==True], Net]

p = prime_list(1000000)[0]
p_bools = prime_list(1000000)[1]

while True:
    N = int(input())
    if N==0:
        break
    for i in range(N//2):
        if p_bools[N-p[i]] == True:
            print(str(N)+ ' = '+ str(p[i])+ ' + '+str(N-p[i]))
            break







