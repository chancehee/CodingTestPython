'''
그리디: <카드 합체 놀이>
'''
import heapq
import sys
n = 4
m = 2

card = list(map(int, sys.stdin.readline().split()))
heapq.heapify(card)

for i in range(m):
    a=heapq.heappop(card)
    b=heapq.heappop(card)
    heapq.heappush(card,a+b)
    heapq.heappush(card,a+b)
print(sum(card))




