#zip() 함수는 두 집합 객체의 원소를 엮는다.


numbers = ['a','b','c']
letters = ["A","B","C"]

score_dic = {l:s for l,s in zip(numbers,letters)}
print(score_dic)
# >>> {a:A, b:B, c:C}

for pair in zip(numbers,letters):
    print(pair)
    #>>> (a:A)
    #>>> (b:B)
    #>>> (c:C)
    #값은 튜플 타입

