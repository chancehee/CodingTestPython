'''
그리디알고리즘: <카드 정렬하기>
문제
정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.
이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다.
예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

출력
첫째 줄에 최소 비교 횟수를 출력한다.
'''

# 문제를 잘못 생각했다. 만약 같은 숫자라면 순차적으로 넣는 것보다 2개씩 묶는 것이 최소이다.

'''
n = int(input())
card_list=[]
for _ in range(n):
    card_list.append(int(input()))

dict={}
dict2={}
card_list.sort()
for i in range(0,n):
    dict[i+1]=card_list[i]

for i in range(1,n):
    dict2[i]=dict[i]+dict[i+1]
    dict[i+1]=dict[i]+dict[i+1]

if n==1:
    print(sum(card_list))
else:
    print(sum(dict2.values()))
'''

#코드는 구현하였지만 시간초과..
'''
data=[]
n = int(input())
card_list=[]
for _ in range(n):
    card_list.append(int(input()))
card_list.sort()

if len(card_list)==1:
    print(card_list[0])
else:
    while len(card_list)> 1:
        m1 = min(card_list)
        card_list.remove(m1)
        m2 = min(card_list)
        card_list.remove(m2)
        card_list.append(m1+m2)
        data.append(m1+m2)
    print(sum(data))
'''
# 질문 조언: 힙 구조체 사용 등 입력과 삭제에서 시간을 줄일 수 있는 구조체 만들거나 사용하기
#힙 구조체를 공부하여 적용해보자!
# 힙 구조체를 공부한후 사용하니 시간 초과를 피했다.
import sys
import heapq
data={}
n = int(sys.stdin.readline())
card_list=[]
cnt=0
for _ in range(n):
    card_list.append(int(input()))

heapq.heapify(card_list)
if len(card_list)==1:
    print(0)
else:
    while len(card_list) > 1:
        m1 = heapq.heappop(card_list)
        m2 = heapq.heappop(card_list)
        heapq.heappush(card_list, m1+m2)
        data[cnt]=(m1 + m2)
        cnt +=1
    print(sum(data.values()))



