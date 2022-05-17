"""
DP: <쉬운 계단 수>

1. 아이디어:
    생각이 나지 않아서 블로그 글을 참조하여 이해해 보았다.
    문제에서 45656 처럼 각 자리수에서 차이가 1이 나는 경우를 계단수라고 정의한다.
    N = 1, 가능한 숫자는 0,1,2,3,4,5,6,7,8,9 가 존재하고 0으로 시작하는 숫자는 없기 때문에 총 개수 10에서 1을 빼준다. 9
    N = 2, 가능한 숫자는 (0-1),(1-0,1-2),(2-1,2-3), ... (8-7,8-9),(9-8) 총 개수 18에서 1을 빼준다. 17
    N = 3, 가능한 숫자는
    0-1-0, 0-1-2 : 2개
    1-0-1, 1-2-1, 1-2-3 : 3개
    2-1-0. 2-1-2. 2-3-2. 2-3-4 : 4개
    ...
    8-7-6, 8-7-8, 8-9-8 : 3개
    9-8-7, 9-8-9 : 2개
    총 개수 34에서 2를 빼준다. 32

    예를 들어 N = 100인 경우에는 N = 1인 경우 ~ N = 99인 경우를 모두 메모이 제이션하여 N = 100인 경우를 구할 수 있다.

    핵심은 0으로 시작하는 숫자가 없어도 개수를 체크하고 총 합에서 빼주는 것이다.
"""

N = int(input())
dp_current = [1] * 10

for i in range(N-1):
    dp_next = [0] * 10
    for j in range(10):
        if j == 0:
            dp_next[j] = dp_current[1]
            continue

        if j == 9:
            dp_next[j] = dp_current[8]
            continue

        dp_next[j] = dp_current[j-1] + dp_current[j+1]

    dp_current = dp_next

print((sum(dp_current)-dp_current[0]) % 1000000000 )
