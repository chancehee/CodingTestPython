'''
그리디: <폴리오미노>
'''

board = "XXXXXX"

result = 0
a = list(board.split('.'))
for k,i in enumerate(a):
    if len(i)%2 ==1:
        result = -1
        break
    elif len(i)==2:
        a[k] = "BB"
    else:
        x = len(i)//4
        y = (len(i)%4)//2
        a[k] = "AAAA"*x + "BB"*y

if result == -1:
    print(-1)
else:
    print(('.').join(a))










