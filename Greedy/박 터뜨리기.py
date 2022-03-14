'''
그리디: <박 터뜨리기>
'''

'''
6 3 -> 1 2 3 : 2 이때는 (n - k까지의합) % k == 0 
7 3 -> 1 2 4 : 3
8 3 -> 1 3 4 : 3
9 3 -> 2 3 4 : 2
10 3 -> 2 3 5 : 3
'''

n,k = map(int, input().split())

basic_sum = int((k * (k + 1)) / 2)

if basic_sum > n:
    print(-1)
elif (n-basic_sum) % k == 0:
    print(k - 1)
else:
    print(k)






