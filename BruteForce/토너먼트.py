"""
브루트포스: <토너먼트>

1. 아이디어:
    종료 조건: 1. n == 1 이면 종료 (모든 토너먼트를 치룬 경우) : -1 출력
               2. a와 b가 만단 경우 종료 : 몇 라운드인지 출력
    반복문을 통해서 n,a,b를 절반으로 나눠가며 상태변화와 만났는지 체크하기.
    n % 2 == 1 인 경우에(홀수인 경우) 부전승 : n // 2
2. 시간복잡도:
    n이 10만인 경우
"""
# 풀이시간: 53분 (a,b 둘의 숫자가 b가 당연히 크다고 생각하여 계속 틀렸다..)

# 참가자 수, 김지민, 임한수
n, a, b = map(int, input().split())
# 라운드 수
cnt = 0


# 김지민과 임한수가 만나는 라운드 수 출력, 없다면 -1 출력( 무조건 이기기 때문에 만나지 않을 경우는 없다.)
def solve(n, a, b):
    global cnt
    while True:
        cnt += 1
        if possible(a, b):
            print(cnt)
            break

        if n == 1:
            print(cnt)
            break

        n = n // 2

        if a % 2 == 1:
            a = a // 2 + 1
        else:
            a = a // 2

        if b % 2 == 1:
            b = b // 2 + 1
        else:
            b = b // 2


# 둘의 대결이 성립하는지 판단하는 함수.
def possible(x, y):
    if x < y:
        if x % 2 == 1 and y-x==1:
            return True
        else:
            return False
    else:
        if y % 2 == 1 and x - y==1:
            return True
        else:
            return False


solve(n, a, b)