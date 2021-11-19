'''
수학: <Fly me to the Alpha Centauri>
'''
# 모든 경우를 수기로 작성하여 패턴을 찾아냈다.
n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    dis = y - x
    cnt = 0

    a = 1
    b = 0
    while dis > b:

        cnt += 1
        b = b + a

        if cnt % 2 == 0:
            a += 1
    print(cnt)
