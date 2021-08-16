'''
그리디알고리즘: <A -> B>
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
'''

a,b = input().split()


cnt = 0
while True:
    if b==a:
        print(cnt+1)
        break
    elif b=='1':
        print(-1)
        break

    if b[-1]=='1':
        b = b[:-1]
        cnt = cnt +1
    elif int(b)%2==1:
        print(-1)
        break
    else:
        b = int(b) // 2
        b = str(b)
        cnt = cnt +1




