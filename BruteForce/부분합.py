'''
브루트포스: <부분합>
'''

n=216
result = 0
for i in range(1,n+1):
    A = list(map(int,str(i)))
    result = i+sum(A)

    if result == n:
        print(i)
        break

else:
    print(0)




