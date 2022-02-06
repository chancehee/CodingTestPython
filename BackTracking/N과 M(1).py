'''
백트래킹: <N과 M>
'''

n,m = map(int, input().split())

rs = []
chk = [False] * (n+1)

def recursion(num):

    if num == m:
        print(*rs)
        return

    for i in range(1,n+1):
        if chk[i] ==  False:
            chk[i] = True
            rs.append(i)
            recursion(num+1)
            # 원상복귀 과정
            chk[i] = False
            rs.pop()

recursion(0)