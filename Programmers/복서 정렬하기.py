'''
프로그래머스(level1): <복서 정렬하기>
'''

# 람다식을 이용한 리스트 정렬법을 배웠다. (여러개의 조건으로 정렬하는 방법)
weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]

boxer_info = []
answer = []

for i in range(len(weights)):
    win_rate = 0
    heavy_cnt = 0
    win_cnt=0
    cnt = 0
    for j in range(len(weights)):
        if i != j:
            if head2head[i][j] != 'N':
                cnt = cnt +1
            if head2head[i][j] == 'W':
                win_cnt = win_cnt + 1
                if weights[i] < weights[j]:
                    heavy_cnt = heavy_cnt + 1
    if cnt == 0:
        win_rate = 0
    else:
        win_rate = win_cnt / cnt
    boxer_info.append((i+1,win_rate,heavy_cnt,weights[i]))

    # 이 부분을 배웠다.
    boxer_info = sorted(boxer_info, key=lambda x: (x[1],x[2],x[3], -x[0]),reverse=True)
    # 그러나 파이썬에서 sort()함수는 동률이면 그 다음 요소를 보고 정렬을 한다
    # 내부적으로 그런 기능으로 동작한다는 것을 숙지하자!!
for i in range(len(boxer_info)):
    answer.append(boxer_info[i][0])

print(answer)





