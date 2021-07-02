'''
Heap: 특정한 규칙을 가지는 트리로 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로한다.
    특징
        A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다.

    분류
        -최소힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
        -최대힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

    파이썬 힙 자료구조
        import heapq //최소 힙 구조
        -추가: heapq.heappush(heap, item)
        -삭제: heapq.heappop(heap)  // 힙에서 가장 작은 원소를   pop (비어 있는 경우 IndexError가 호출됨)
        -변환: heapq.heapify(x) // 리스트 x를 즉각적으로 힙으로 변환함 O(N)
'''

import heapq # 최소 힙
a = [9,3,5,7,9]
heapq.heapify(a)  # 힙 구조로 변환
print(a)

m1=heapq.heappop(a)
m2=heapq.heappop(a)
print(m1,m2)

m3=a[0] # 원소를 삭제하기 않고 가져오기
print(m3)

#최대 힙
#힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.

b = [1,3,5,7,9]

max_heap = []
for item in b:
    heapq.heappush(max_heap, (-item,item))

print(max_heap)

max_item = heapq.heappop(max_heap)[1]
print(max_item)
