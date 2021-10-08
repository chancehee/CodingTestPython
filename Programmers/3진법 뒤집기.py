'''
프로그래머스(level1): <3진법 뒤집기>
'''

n = 125
num3 = []



while (n//3 > 0):
    remain = n%3
    n = n // 3
    num3.append(str(remain))
num3.append(str(n))

a = ''.join(num3)
print(int(a,3))



