'''
브루트 포스 : <유레카 이론>
1000의 값까지 반복하여 삼각수 배열을 만든다.
삼각수를 3번 사용하여 만들 수 있는지 검사.(반복문 3번) -> 모든 3가지의 합 검사
ex)
tri = [1,3,6,10,15,21,28,36,45,55, ... ]
1+1+1
1+1+3
1+1+6
...
1+3+1
1+3+3
1+3+6
...
이런식으로 반복

3가지 수의 합이 1000보다 작을 경우에 eureka배열에 1을 담는다. 아닌 경우엔 0
'''

tri_nums = [1]
for i in range(2,46):
    tri_nums.append(tri_nums[-1] + i)

eureka = [0] * 1001
for i in tri_nums:
    for j in tri_nums:
        for k in tri_nums:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1

# t개의 입력을 반복, n이 3개의 삼각수로 더해질 수 있는지 검사
t = int(input())
for i in range(t):
    n = int(input())
    print(eureka[n])