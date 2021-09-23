'''
프로그래머스(level1): <가운데 글자 가져오기>
'''

s = 'q'

if len(s)%2==0: #짝수이면
    mid = len(s)//2 - 1
    print(s[mid:mid+2])
else:
    mid = len(s)//2
    print(s[mid])
