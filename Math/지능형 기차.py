'''
그리디: <지능형 기차>
'''

data = []

for i in range(4):
    data.append(list(map(int, input().split())))

result = [data[0][1]]
for i in range(1,4):
    result.append( data[i-1][1] - data[i][0] + data[i][1] )
    data[i][1] = result[-1]
print(max(result))


