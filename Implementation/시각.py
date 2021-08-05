'''
구현: <시각>
00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수를 출력

'''

#완전 탐색 문제 유형 (브루트 포씽)
#파이썬: 1초에 2천만번 연산 수행
#하루는 86400초

N = int(input())
cnt = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt = cnt+1

print(cnt)



