'''
입력
 1.input() 함수
    -기본이다
    -리스트형태로 입력 받을 때(입력시 공백 있음)
        list(map(int, input().split()))
 2.readline() 함수
    -입력의 개수가 많은 경우 시간을 단축 시키기 위한 방법
        import sys
        sys.stdin.readline().rstrip()
        rstrip()이란? : readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백
                        문자를 제거하려면 rstrip()함수를 사용해야한다. (꼭 외우기)

출력
 1.print() 함수

 2.f-string 문법
    파이썬 3.6 이상의 버전부터 문법사용가능
    문자열 앞에 접두사 'f'를 붙임으로써 사용

'''

#자료형의 변환 없이 문자열과 정수를 함께 사용할 수 있다.
answer=7
print(f"정답은 {answer}입니다.")
