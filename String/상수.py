'''
문자열: <상수>

아이디어: A,B 를 거꾸로 만든다  -> max() 사용 출력
A[::-1] : extended slices, 처음부터 끝까지 -1칸 간격으로 (역순으로)
'''

A,B = input().split()
print(A[::-1])
A = list(A)
re_A = ''
for i in range(len(A)):
    re_A = re_A + A.pop()

B = list(B)
re_B = ''
for i in range(len(B)):
    re_B += B.pop()

print(max(int(re_A),int(re_B)))



