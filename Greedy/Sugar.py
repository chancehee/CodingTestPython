'''
그리디알고리즘: <설탕 배달>
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다.
봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''



''' //코드는 작동하나 런타임에러 발생함
N = int(input())
count=[1e9]

m=N//5

for i in range(1,m+1):
    if (N-5*i)%3==0:
        count.append(i+(N-5*i)//3)

if N%5==0:
    count.append(N//5)

if N%3==0:
    count.append(N//3)

if min(count)==1e9:
    print(-1)
else:
    print(min(count))
'''

#따라서 집합과 for문을 수정함 -> 성공
N = int(input())
count = set([1e9])
M = N//5
if N%5==0:
    count.add(N//5)
elif N%3==0:
    count.add(N//3)
for i in range(M,0,-1):
    if (N-5*i)%3==0 and min(count)>(i+(N-5*i)//3):
        count.add(i+(N-5*i)//3)
if min(count)==1e9:
    print(-1)
else:
    print(min(count))

print(count)