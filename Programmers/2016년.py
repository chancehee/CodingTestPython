'''
프로그래머스(level1): <2016년>

'''

#윤년(4로 나누어 떨어지는 년도)은 한국에서는 2월 29일 하루를 추가해주면 된다.

# 2016 01 01 = 금요일
# 2016 05 24 = 화요일


#내 풀이 하드코딩..
'''
a=1
b=7
def solution(a, b):
    if a == 1 or a == 4 or a == 7:
        weeks = {1: 'FRI', 2: 'SAT', 3: 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED', 7: 'THU'}
    elif a == 2 or a == 8:
        weeks = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'}
    elif a == 3 or a == 11:
        weeks = {1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN', 7: 'MON'}
    elif a == 5:
        weeks = {1: 'SUN', 2: 'MON', 3: 'TUE', 4: 'WED', 5: 'THU', 6: 'FRI', 7: 'SAT'}
    elif a == 6:
        weeks = {1: 'WED', 2: 'THU', 3: 'FRI', 4: 'SAT', 5: 'SUN', 6: 'MON', 7: 'TUE'}
    elif a == 9:
        weeks = {1: 'THU', 2: 'FRI', 3: 'SAT', 4: 'SUN', 5: 'MON', 6: 'TUE', 7: 'WED'}
    elif a == 10:
        weeks = {1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU', 7: 'FRI'}
    elif a == 12:
        weeks = {1: 'THU', 2: 'FRI', 3: 'SAT', 4: 'SUN', 5: 'MON', 6: 'TUE', 7: 'WED'}

    key = b % 7
    return (weeks.get(key))
print(solution(a,b))
'''
a=3
b=1
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
print(getDayName(a,b))



