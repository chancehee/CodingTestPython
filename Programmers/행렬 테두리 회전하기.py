'''
프로그래머스(level2): <행렬 테두리 회전하기>
'''

# 1. 초기 행렬 값 구하기: 딕셔너리를 이용하여 구현 ( 초기에 숫자로면 구현시 문제점 발견 ) 문제점: 22행3열이랑 2행23열이랑 같은 키값을 사용하는 문제
# 따라서 행 과 열을 붙여서 key값 수정

# 2. 테두리를 시계방향으로 한 칸씩 옮기기 위해서 첫 번째 변수를 temp에 담고 나머지를 while 문을 통하여 4개의 테두리별로 구현

# 3. 테두리 중에서 가장 작은 값을 결과에 넣어야 하므로 result 배열에 테두리중에서 min값인 m을 append처리

# 풀이시간: 1시간30분 / 느낀점: 아이디어를 코드로 구현하는 시간이 너무 오래걸렸던 것 같다... 구현 실력을 키워서 추후에는 시간 단축을 도모한다.



def solution(rows, columns, queries):
    graph = {}
    result = []

    c = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            graph[str(i) + '행' + str(j) + '열'] = c
            c += 1

    for h in queries:
        x_min = h[0]
        x_max = h[2]

        y_min = h[1]
        y_max = h[3]

        now_x = h[0]
        now_y = h[1]
        temp = graph[str(x_min) + '행' + str(y_min) + '열']
        m = temp

        while (now_x != x_max):

            if graph[str(now_x + 1) + '행' + str(now_y) + '열'] < m:
                m = graph[str(now_x + 1) + '행' + str(now_y) + '열']
            graph[str(now_x) + '행' + str(now_y) + '열'] = graph[str(now_x + 1) + '행' + str(now_y) + '열']
            now_x = now_x + 1

        # 현재 (5,2)
        while (now_y != y_max):

            if graph[str(now_x) + '행' + str(now_y + 1) + '열'] < m:
                m = graph[str(now_x) + '행' + str(now_y + 1) + '열']
            graph[str(now_x) + '행' + str(now_y) + '열'] = graph[str(now_x) + '행' + str(now_y + 1) + '열']
            now_y = now_y + 1

        # 현재 (5,4)
        while (now_x != x_min):

            if graph[str(now_x - 1) + '행' + str(now_y) + '열'] < m:
                m = graph[str(now_x - 1) + '행' + str(now_y) + '열']
            graph[str(now_x) + '행' + str(now_y) + '열'] = graph[str(now_x - 1) + '행' + str(now_y) + '열']
            now_x = now_x - 1

        # 현재 (2,4)
        while (now_y != y_min):

            if graph[str(now_x) + '행' + str(now_y - 1) + '열'] < m:
                m = graph[str(now_x) + '행' + str(now_y - 1) + '열']
            graph[str(now_x) + '행' + str(now_y) + '열'] = graph[str(now_x) + '행' + str(now_y - 1) + '열']
            now_y = now_y - 1

        graph[str(now_x) + '행' + str(now_y + 1) + '열'] = temp

        result.append(m)

    return result
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(6,6,queries))






