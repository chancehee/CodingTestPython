#최소 거스름돈_그리디 알고리즘
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count = count + n//coin
    n = n%coin

print(count)


