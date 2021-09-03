'''
직업군 추천하기
'''

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["JAVA","JAVASCRIPT"]
preference = [7,5]

#내풀이
'''
def solution(table, languages, preference):
    a=table[0].split()
    b=table[1].split()
    c=table[2].split()
    d=table[3].split()
    e=table[4].split()
    collect = [a,b,c,d,e]
    subject = [a[0],b[0],c[0],d[0],e[0]]
    result_list = []
    score =0
    for n in range(5):
        result = 0
        for i in range(len(languages)):
            try:
                idx = collect[n].index(languages[i])
                if idx==1:
                    score=5
                elif idx==2:
                    score=4
                elif idx==3:
                    score=3
                elif idx==4:
                    score=2
                elif idx==5:
                    score=1
            except:
                score=0

            result = result + preference[i]*score
        result_list.append(result)
    p = max(result_list)
    ex_list = []
    c = result_list.count(p)

    if c>=2:
        for i in range(5):
            if result_list[i]==p:
                ex_list.append(subject[i])
        sorted_ex_list = sorted(ex_list)
        answer = sorted_ex_list[0]
    else:
        answer = subject[result_list.index(p)]
    return answer

print(solution(table,languages,preference))
'''

#다른 사람 풀이
#zip, get, 알파벳 관계연산 가능 // 을 배웠다.
def solution(table,languages,preference):
    answer = 'zzz'
    score_dic = {lang: score for lang, score in zip(languages,preference)}
    print(score_dic)
    # JAVA: 7 , JAVASCRIPT: 5
    max_score = 0

    for row in table:
        r = row.split()
        #r = [SI JAVA JAVASCRIPT SQL PYTHON C#]
        curr_score = 0
        for i in range(1,len(r)):
            curr_score = curr_score + score_dic.get(r[i],0) * (6-i) # 7*5 + 5*4 = 55
        if max_score < curr_score:
            max_score = curr_score
            answer = r[0]
        elif max_score == curr_score and answer > r[0]: #S 가 P보다 사전순서로 뒤에 있기 때문에
            answer = r[0]
    return answer

print(solution(table,languages,preference))
