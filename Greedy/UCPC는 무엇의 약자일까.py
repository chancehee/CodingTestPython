'''
그리디: <UCPC는 무엇의 약자일까?>
'''

data = input()

word = "UCPC"

idx = 0

for i in data:
    if idx == 4:
        break

    if i==word[idx]:
        idx += 1

if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")






