'''
구현: 문자열 재정렬
'''
#배운점1: x.isalpha() // x가 문자인지 체크
#배운점2: ''.join() // 구분자가 없이(공백없이) 이어준다
S = input()
arr =[]
s=0
for i in S:
    if i.isalpha():
       arr.append(i)
    else:
        s=s+int(i)

arr.sort()

if s != 0:
    arr.append(str(s))

print(''.join(arr))



