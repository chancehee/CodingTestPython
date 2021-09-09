'''
프로그래머스(level1): <완주하지 못한 선수>

'''
#10만명 연산
#collections 의 쓰임을 공부하였다.
#뺄셈 연산 가능
import collections

participant = ['mislav','stanko','mislav','ana']
completion = ['stanko','ana','mislav']

result = list(collections.Counter(participant) - collections.Counter(completion))
print(result[0])











