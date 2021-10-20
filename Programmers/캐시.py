'''
프로그래머스(level2) : <캐시>
'''

# LRU란 가장 오랫동안 참조되지 않은 페이지를 교체하는 방법


from collections import deque

cacheSize = 2
cache = deque()


cities =["Jeju", "Pangyo", "NewYork", "newyork"]
result = 0

if cacheSize == 0:
    print(len(cities)*5)

for i,c in enumerate(cities):
    a = c.lower()
    if a in cache:
        result += 1
    else:
        result += 5

    # pop연산도 수행
    if len(cache)==cacheSize:
        if a in cache:
            cache.remove(a)
            cache.append(a)
        else:
            cache.popleft()
            cache.append(a)
    else:
        if a not in cache:
            cache.append(a)
        else:
            cache.remove(a)
            cache.append(a)

print(result)

