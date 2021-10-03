'''
프로그래머스(level1): <문자열 내 마음대로 정렬하기>
'''


strings = ["abaz", "abaa", "zzab"]
n = 2

# 앞 부분 / 뒷 부분
# 1. 앞부분으로 정렬
# 2. 인덱스 부분이 같은 문자일 경우 -> 뒷부분을 통해 정렬

strings = sorted(strings, key=lambda x:(x[2],x[:2],x[3:]))
print(strings)













