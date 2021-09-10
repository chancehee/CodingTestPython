'''
프로그래머스(level1): <체육복>
'''
n = 3
lost = [3]
reserve = [1]

student = [1 for i in range(1,n+1)]
for i in range(len(student)):
    if i+1 in lost:
        student[i] = student[i]-1
    if i+1 in reserve:
        student[i] = student[i]+1

i=0
while True:
    #종료 조건
    if i == n:
        break
    #앞 채우고 뒤 채우기
    if student[i] == 0 or student[i]==1:
        i = i +1
        continue
    else:
        try:
            if i!=0 and student[i-1]==0:
                student[i-1]=1
                student[i]= 1
                i = i+1
                continue
            elif student[i+1]==0:
                student[i+1]=1
                student[i] = 1
                i = i+1
                continue
            else:
                i=i+1
                continue
        except:
            i=i+1
            continue

print(len(student) - student.count(0))













