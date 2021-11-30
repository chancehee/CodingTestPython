'''
그리디: <보물>
'''

N = int(input())
A = [1,1,3]
B = [10,30,20]

B.sort()
A.sort(reverse=True)

s = 0
for i in range(N):
    s = s+ A[i]*B[i]

print(s)