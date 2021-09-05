'''
프로그래머스(level1): <숫자 문자열과 영단어>
'''

s = "2three45sixthree"

nums = ['zero','one','two','three','four','five','six','seven','eight','nine']

for idx,num in enumerate(nums):
    if num in s:
        s= s.replace(num,str(idx))
print(int(s))
