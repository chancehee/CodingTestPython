'''
브루트포스: <스타트와 링크>
'''

'''
1. 아이디어
    0번 ~ N - 1번 까지 
    팀을 2개로 나누어 팀원이 되는 모든경우에서 구성원 능력치의 합의 차가 최소가되는 것을 구한다.
    1) 팀을 둘로 나누기 (중복 x)
    2) 나누었을때 능력치 차이 계산 -> 최소인 경우 업데이트

2. 시간복잡도
    
     
3. 변수명

'''

answer = 1e9
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 팀에 따라 모든 능력치를 합하는 함수.
def cal_diff(team1, team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team2)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


# N개의 수를 중복없이 2개의 팀으로 나누는 방법
def make_team(team1, count, N, start):
    global answer

    # 팀을 2개로 나누는 과정 (team1을 먼저 채우고 가득차면 나머지 team2를 채운다.)
    if count == N/2:
        team2 = []
        for i in range(N):
            if i not in team1:
                team2.append(i)
        # print(team1, team2)

        # 나눠진 팀으로 능력치를 비교하기
        local_diff = cal_diff(team1,team2)
        answer = min(answer, local_diff)
        return

    # 핵심 부분
    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            make_team(team1, count+1, N, i+1)
            team1.remove(i)


make_team([], 0, N, 0)
print(answer)




