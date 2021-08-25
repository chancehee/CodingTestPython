#get() 함수 ////사전자료형에서 사용한다
'''
    get(a,b): 첫 번째 인자에 찾고 싶은 딕셔너리 key 값을 입력
              두 번째 인자에 첫 번째 인자가 없을 경우 출력하고 싶은 값 입력
              key값의 value 값 출력.
'''

name = {
    'chan':26,
    'yujin':22
}

result = name.get('c',999)
print(result)