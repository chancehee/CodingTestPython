'''
프로그래머스(level1) : <문자열 내림차순으로 배치하기>
'''

s = 'aAbBcC'
s_list=sorted(s,reverse=True)
print("".join(s_list))

