'''
그리디: <사과 담기 게임>
'''

n,m = map(int, input().split())
r = int(input())
data = []
for i in range(r):
    data.append(int(input()))


start = 1
end = m
interval = end-start
cnt = 0
for d in data:

    if start<= d <= end:
        continue
    else:
        if d > end:
            diff = d - end
            start += diff
            end += diff
            if end >= n:
                end = n
                start = n - interval
            cnt += diff
        elif d < start:
            diff = start - d
            start -= diff
            end -= diff
            if start <= 1:
                start = 1
                end = 1 + interval
            cnt += diff

print(cnt)





