"""
D2 1979. 어디에 단어가 들어갈 수 있을까

1. 아이디어:
    N x N 크기의 단어 퍼즐에서, 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수 출력하기.
    문제에서 주어진 설명이 빈약하다고 생각한다.
    테스트 케이스를 살펴보면, K길이와 동일한 빈칸이 존재할 경우 count + 1 해준다.
    i) 가로를 기준으로 살펴본다.
    ii) 세로를 기준으로 살펴본다.
    split() 함수 활용.

"""


T = int(input())


# 90도 회전 행렬 만들기
def make_90_arr(arr, N):
    a = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a[i].append(arr[N - j - 1][i])

    return a


for tc in range(T):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # solve 함수 만들기
    count = 0
    for i in arr:
        c = str(i)[1:-1].replace(',', "")
        c = c.replace(" ", "")
        c = c.split('0')
        for j in c:
            if len(j) == K and j != '':
                count += 1

    a = make_90_arr(arr, N)
    for i in a:
        c = str(i)[1:-1].replace(',', "")
        c = c.replace(" ", "")
        c = c.split('0')
        for j in c:
            if len(j) == K and j != '':
                count += 1

    print("#{} {}".format(tc+1, count))
