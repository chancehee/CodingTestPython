'''
프로그래머스(level2): <H-Index>
'''

citations = [41,24]


citations.sort()

for i in range(1,len(citations)+1):
    min_num = citations[-i]

    if min_num >= i:
        answer = i
    print(min_num, i,answer)
print(answer)


