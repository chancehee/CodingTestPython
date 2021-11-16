'''
프로그래머스(level2) : <전력망을 둘로 나누기>
'''
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

# google -> "how to append an element to a key in a dictionary with Python
# 1.a_dict = collections. defaultdict(list)
# 2.a_dict["a"]. append("hello")
# 3.print(a_dict)
# 4.a_dict["a"]. append("kite")
# 5.print(a_dict)

# defaultdict란? 초기값을 지정해주는 사전 자료형

# 유니온파인드를 쓰는 방법도 있다.

from collections import defaultdict

result = []
graph = defaultdict(list)

for a,b in wires:
    graph[a].append(b)
    graph[b].append(a)
print(graph)

def dfs(i, visited):
    global cnt
    visited.append(i)
    cnt = cnt + 1
    for i in graph[i]:
        if i not in visited:
            dfs(i,visited)

for a,b in wires:
    graph[a].remove(b)
    graph[b].remove(a)
    cnt = 0

    dfs(1,[])
    print(cnt)
    result.append(abs(n - 2*cnt))
    graph[a].append(b)
    graph[b].append(a)
# 두 그룹의 통신탑 개수의 차이
print(result)
print(min(result))



