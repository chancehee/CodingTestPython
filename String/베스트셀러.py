'''
문자열: <베스트셀러>
'''

N = int(input())
word_dic = {}
for i in range(N):
    word = input()

    if word not in word_dic:
        word_dic[word] = 1
    else:
        word_dic[word] = word_dic[word] + 1

m = max(word_dic.values())

answer = []
for i in word_dic:
    if word_dic[i] == m:
        answer.append(i)

answer.sort()
print(answer[0])



