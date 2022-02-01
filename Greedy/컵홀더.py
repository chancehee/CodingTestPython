'''
그리디: <컵홀더>
'''

n = int(input())
data = input()

data = data.replace('LL','L')


if len(data) >= n:
    print(n)
else:
    print(len(data)+1)





