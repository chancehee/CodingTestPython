'''
프로그래머스(level1): <신규 아이디 추천>
'''

# 아이디 길이 3~15
# 소문자 숫자 - _ . 사용가능
# . 는 처음과 끝에 사용못하고 연속으로 사용 못함
# 7 단계
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
# 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

new_id = "......abcdefghijklmn.p"
#1단계
def first(string):
    string = string.lower()
    return string

#2단계
def second(string):
    target = "~!@#$%^&*()=+[{]}:?,<>/"
    string = ''.join(i for i in string if i not in target)
    return string

#3단계
def third(string):
    while ('..' in string):
        string = string.replace('..','.')
    return string

#4단계
def fourth(string):
    if string=="":
        return string

    if string[0] == '.':
        string = string.replace('.','',1)
        if string=="":
            return string

    if string[-1]=='.':
        if len(string)==1:
            string = ''
        else:
            string = string[:-1]
    return string

#5단계
def fifth(string):
    if string == '':
        string = 'a'
    return string

#6단계
def sixth(string):
    if len(string)>15:
        string = string[:15]
    if string[-1]=='.':
        string = string[:-1]
    return string

#7단계
def seventh(string):
    end = string[-1]
    if len(string)<3:
        while True:
            if len(string)==3:
                return string
                break
            string = string + end
    else:
        return string

print(seventh(sixth(fifth(fourth(third(second(first(new_id))))))))





