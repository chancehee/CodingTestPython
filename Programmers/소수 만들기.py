'''
프로그래머스(level1): <소수 만들기>
'''

# 숫자 중 3개를 더해서 소수가 되는 경우의 개수 출력하기
# 숫자 3 ~ 50 개 --> 예상 시간 복잡도 50 C 3 = 31850번 연산
import itertools
import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

nums = [1,2,7,6,4]

a = list(itertools.combinations(nums,3))
cnt = 0
for n in a:
    if is_prime_number(sum(n)):
        cnt = cnt+1
print(cnt)

