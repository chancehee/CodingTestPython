'''
프로그래머스(level2): <큰 수 만들기>
'''
import heapq

# k개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자 , 순서는 지켜야한다.
# 리스트 원소 백만개
# 작은 숫자를 제거할 때에도 순서는 지켜야한다.
# 아이디어: 스택에 숫자를 넣는다 숫자를 넣을 때 이미스택에 있는 숫자가 들어오는 숫자보다 작다면 아웃 count 감소
#           숫자 문자열을 다 돌았을 때 count가 남아있다면 이미 스택에 있는 숫자보다 작거나 같은수 이므로 count만큼 제거


number = "4177252841"
k = 4

stk = []

for i in number:
    while stk and stk[-1] < i and k>0:
        k = k - 1
        stk.pop()
    stk.append(i)
    print(stk,k)
result = "".join(stk[:len(stk)-k])
print(result)




