'''
프로그래머스(level1): <비밀지도>
'''

n = 5

arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]
answer = []
for i in range(n):
    k=bin(arr1[i] | arr2[i])[2:]
    if len(k)==n:
        pass
    else:
        diff=n-len(k)
        k=diff*'0'+k
    k=k.replace('1','#')
    k=k.replace('0'," ")
    answer.append(k)
print(answer)

