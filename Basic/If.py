'''
조건문: 프로그램의 흐름을 제어하는 문법
문법: if ~ elif ~ else
들여쓰기 = 스페이스바 4번  또는 Tab  (두 진영에 대한 논쟁은 지금도 활발하다)
연산자:
    -비교 연산자
    -논리 연산자
    -기타 연산자:
        in
        not in
        pass: 조건문이 참이라고 해도, 아무것도 처리하고 싶지 않을 때 이용.
'''

'''
<리스트에서 특정한 원소의 값을 없애기>
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)
'''