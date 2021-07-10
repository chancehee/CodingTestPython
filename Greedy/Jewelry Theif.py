'''
그리디알고리즘: <보석 도둑>
문제
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
상덕이가 털 보석점에는 보석이 총 N개 있다.
각 보석은 무게 Mi와 가격 Vi를 가지고 있다.
상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다.
 가방에는 최대 한 개의 보석만 넣을 수 있다.
상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.


'''

#느낀점: 힙구조에 대한 공부필요
#아이디어: 시간문제를 생각해 최대힙 자료구조 활용 / 조건을 만족하는 보석들의 모든 값을 heap구조에 담고 그중에서 가방갯수 만큼 가장큰값 더한다.

import sys
import heapq
N,K=map(int, sys.stdin.readline().split())
jewlryList = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] #여러개 배열 2중배열로 입력받기
bagList = [int(sys.stdin.readline()) for _ in range(K)]

jewlryList.sort()
bagList.sort()

result=0
temp=[]
result_list=[]

for i in bagList:
    while jewlryList and i >= jewlryList[0][0]: #최대 무게허용되고 보석갯수만큼 반복
        heapq.heappush(temp, -jewlryList[0][1]) #조건 만족하는 보석 값 다 넣기
        heapq.heappop(jewlryList)
    if temp:
        result_list.append(heapq.heappop(temp)) #가장 작은 수 부터 추가
    elif not jewlryList:
        break

print(-sum(result_list))





