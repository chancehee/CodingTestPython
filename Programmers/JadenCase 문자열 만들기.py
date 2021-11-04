'''
프로그래머스(level2): <JadenCase 문자열 만들기>
'''
# 공백이 여러개인 경우 고려
s = "3people    unFollowed me"

def solution(s):
    s = s.lower()

    s = s.split(" ")
    print(s)

    # 대문자로 변환 하기
    for i in range(len(s)):
        if len(s[i]) != 0 and s[i][0].isalnum():
            up = s[i][0].upper()
            s[i] = up + s[i][1:]
    result = " ".join(s)
    return result

print(solution(s))









