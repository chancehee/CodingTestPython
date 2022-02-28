'''
재귀: <별 찍기 - 10>
'''

def recursion(num):
    # base case
    if num == 3:
        Map[0][:3] = Map[2][:3] = ['*','*','*']
        Map[1][:3] = ['*',' ','*']
        return
    # recursion case
    a = num // 3
    recursion(a)

    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]


n = int(input())
Map = [[' ' for _ in range(n)] for _ in range(n)]
recursion(n)

for m in Map:
    print(''.join(m))

