'''
문자열: <그룹 단어 체커>
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''

# 백준문제는 프린트로 제출 / 프로그래머스는 return으로 제출 
n = int(input())
words = []
for i in range(n):
    words.append(input())

def check(word):
    a = set()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        else:
            if word[i] in a:
                return False
            a.add(word[i])

        if word[-1] in a:
            return False
    return True

def solution(n,words):
    cnt = 0
    for word in words:
        if check(word):
            cnt += 1

    return cnt

print(solution(n,words))







