'''
구현: <숫자의 개수>
'''

ABC = [int(input()) for _ in range(3)]

x = 1
for i in ABC:
    x = x * i


graph = [0 for _ in range(10)]

for i in str(x):
    graph[int(i)] = graph[int(i)]+1

for i in graph:
    print(i)




