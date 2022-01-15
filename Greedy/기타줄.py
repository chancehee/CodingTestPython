'''
그리디: <기타줄>
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

package_price = []
one_price = []
for i in range(m):
    a,b = map(int,input().split())
    package_price.append(a)
    one_price.append(b)
mp = min(package_price)

min_price = min(one_price) * n

if n % 6 != 0:
    x = n // 6 + 1
else:
    x = n // 6

for i in range(1,x+1):
    a = mp * i
    if n - 6*i > 0:
        b = (n-6*i) * min(one_price)
    else:
        b = 0

    s = a + b

    if s < min_price:
        min_price = s

print(min_price)






