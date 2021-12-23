'''
그리디: <5와 6의 차이>
'''

a,b = input().split()

a_min = a.replace('6','5')
b_min = b.replace('6','5')
r1 = (int(a_min)+int(b_min))

a_max = a.replace('5','6')
b_max = b.replace('5','6')
r2 = int(a_max) + int(b_max)

print(r1,r2)

