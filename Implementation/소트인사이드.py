'''
구현 : <소트인사이드>
'''

n = list(input())
n.sort(reverse=True)
answer = "".join(n)
print(int(answer))

