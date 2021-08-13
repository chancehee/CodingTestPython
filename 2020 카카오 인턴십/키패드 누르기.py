numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = "right"






def search(a):
    if a==1:
        x=0
        y=0
    elif a==2:
        x=0
        y=1
    elif a==3:
        x=0
        y=2
    elif a==4:
        x=1
        y=0
    elif a==5:
        x=1
        y=1
    elif a==6:
        x=1
        y=2
    elif a==7:
        x=2
        y=0
    elif a==8:
        x=2
        y=1
    elif a==9:
        x=2
        y=2
    elif a=='*':
        x=3
        y=0
    elif a==0:
        x=3
        y=1
    elif a=='#':
        x=3
        y=2
    aa=[x,y]
    return aa

result=[]

def solution(numbers,hand):
    lx=3
    ly=0

    rx=3
    ry=2
    for i in range(len(numbers)):

        x=search(numbers[i])[0]
        y=search(numbers[i])[1]


        if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
            result.append('L')
            lx=x
            ly=y
        elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
            result.append('R')
            rx=x
            ry=y
        else:
            if abs(lx-x)+abs(ly-y) == abs(rx-x)+abs(ry-y):
                if hand=='right':
                    result.append('R')
                    rx=x
                    ry=y
                else:
                    result.append('L')
                    lx=x
                    ly=y
            elif abs(lx-x)+abs(ly-y) > abs(rx-x)+abs(ry-y):
                result.append('R')
                rx=x
                ry=y
            else:
                result.append('L')
                lx=x
                ly=y
    a = "".join(result)


    return a

print(solution(numbers,hand))

