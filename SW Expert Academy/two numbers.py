"""
D2 1959. 두 개의 숫자열

1. 아이디어:
    숫자 배열 A, B가 있을 때 두 배열의 길이를  비교하여 3가지 경우로 나누어 해결.

"""
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []

    if len(a) < len(b):
        diff = len(b) - len(a)
        for c in range(diff+1):
            temp = 0
            for i in range(len(a)):
                for j in range(len(a)):
                    if i == j:
                        temp += a[i] * b[j+c]
            result.append(temp)

    elif len(a) == len(b):
        temp = 0
        for i in range(len(a)):
            for j in range(len(b)):
                if i == j:
                    temp += a[i] * b[j]
        result.append(temp)
    else:
        diff = len(a) - len(b)
        for c in range(diff+1):
            temp = 0
            for i in range(len(b)):
                for j in range(len(b)):
                    if i == j:
                        temp += b[i] * a[j+c]
            result.append(temp)

    print("#{} {}".format(tc+1, max(result)))