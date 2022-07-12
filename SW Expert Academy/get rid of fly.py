"""
D2 2001. 파리 퇴치

1. 아이디어:
    N x N 배열에서 M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이기.

    M x M 크기로 내려칠 수 있는 모든 경우를 탐색한다.

    N - M
    1일때 4번
    2일때 9번
    3일때 16번
    2 ^ (차이 + 1) 의 경우 탐색
"""

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    search_cnt = N - M + 1

    result = 0
    for i in range(search_cnt):
        for j in range(search_cnt):
            temp = 0
            for k in range(M):
                for h in range(M):
                    temp += arr[i+k][j+h]
            result = max(result, temp)

    print("#{} {}".format(tc+1, result))