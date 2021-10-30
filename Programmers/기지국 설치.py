'''
프로그래머스(level3): <기지국 설치>
'''

n = 11
w = 1
stations = [4,9]


# 내 풀이
# 기지국이 1개인 경우 앞뒤 구하는 로직과
# 기지국이 2개 이상인 경우 앞인경우와 뒤일 경우 그리고 나머지 더하는 경우로 구현하였다.
# 하다보니 너무 하드 코딩이 되었다.. 다른 사람의 코드를 보고 느낀점이 크다..
def solution(n, stations, w):
    result = 0

    # 기지국이 1개일 경우
    if len(stations) == 1:
        # 앞부분
        s = stations[0]
        if (s - w - 1) >= 1:
            start = 1
            end = s - w - 1
            if (end - start + 1) % (2 * w + 1) == 0:
                cnt = (end - start + 1) // (2 * w + 1)
            else:
                cnt = (end - start + 1) // (2 * w + 1) + 1
        else:
            cnt = 0
        result = result + cnt

        # 뒷부분
        if (s + w + 1) > n:
            cnt = 0
        else:
            start = s + w + 1
            end = n
            if (end - start + 1) % (2 * w + 1) == 0:
                cnt = (end - start + 1) // (2 * w + 1)
            else:
                cnt = (end - start + 1) // (2 * w + 1) + 1
        result = result + cnt

        return result

    # 기지국이 두개 이상일 때
    for i, s in enumerate(stations):
        cnt = 0

        # 첫 번째 기지국 : 앞부분 구하기
        if i == 0:
            # 노드 개수가 존재 할 때 -> 구간 내 기지국 몇개 설치?
            if (s - w - 1) >= 1:
                start = 1
                end = s - w - 1

                if (end - start + 1) % (2 * w + 1) == 0:
                    cnt = (end - start + 1) // (2 * w + 1)
                else:
                    cnt = (end - start + 1) // (2 * w + 1) + 1
            # 노드 개수가 0개일 때 -> 기지국 설치 X
            else:
                cnt = 0
        result = result + cnt

        # 맨 마지막 기지국이 아닌 경우
        if i != len(stations) - 1:
            start = s + w + 1
            end = stations[i + 1] - w - 1
            if (end - start + 1) % (2 * w + 1) == 0:
                cnt = (end - start + 1) // (2 * w + 1)
            else:
                cnt = (end - start + 1) // (2 * w + 1) + 1
            result = result + cnt
        # 맨 마지막 기지국인 경우 : 뒷부분 구하기
        else:
            if i == len(stations) - 1:
                if (s + w + 1) > n:
                    cnt = 0
                else:
                    start = s + w + 1
                    end = n
                    if (end - start + 1) % (2 * w + 1) == 0:
                        cnt = (end - start + 1) // (2 * w + 1)
                    else:
                        cnt = (end - start + 1) // (2 * w + 1) + 1
            result = result + cnt
    return result

print(solution(n,stations,w))



# 다른 사람 코드
'''
def solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans
'''







