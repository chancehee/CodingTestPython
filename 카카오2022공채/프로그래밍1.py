id_list = ['muzi','frodo','apeach','neo']
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#id_list = ['con','ryan']
#report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k=2

#시간초과
class person(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'"+self.name+"'"


def reported_list(report):
    x = dict()
    for i in id_list:
        x[i]=[]
    for i in range(len(report)):
        a,b = report[i].split()
        x[a] = []
    reported = dict()
    h = dict()
    h2 = dict()
    reported_name = []
    for i in range(len(report)):
        a,b = report[i].split()
        if b not in x[a]:
            x[a].append(b)
        #만약 동일인 이면 신고횟수 증가 X
        if b in reported and h2.get(b) != a:
            reported[b] = reported.get(b)+1
            h[person(b)]=a
            h2[b]=a
        else:
            h[person(b)]=a
            h2[b]=a
            reported[b] = 1

    for i in reported:
        if reported.get(i)>=k:
            reported_name.append(i)



    result = []

    #신고자 이름을 신고했다면 +1
    for i in x:
        cnt = 0

        for id in reported_name:
            if id in x[i]:
                cnt = cnt + 1
        result.append(cnt)

    return result


reported_list(report)



