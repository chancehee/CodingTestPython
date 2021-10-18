'''
프로그래머스(level2) : <가장 큰 수>
'''
# 처음에 당연하게 순열을 생각하여 풀어보려 하였지만, 시간초과 O(n!) 이기 때문이다.
# 따라서 숫자의 앞머리부터 큰수가 올 수 있게 정렬을 한다면 풀이가 가능하다고 아이디어를 떠올렸다.
# 하지만 자리수의 out of range 에러 때문에 고민하다가 블로그 글 참조
# 숫자를을 3번 곱해주고 정렬처리 (3번: 숫자가 1000이하의 숫자이므로)

numbers = [0,0,0]
num = list(map(str,numbers))
num.sort(key=lambda x:x*3, reverse=True)

print(str(int(''.join(num))))







