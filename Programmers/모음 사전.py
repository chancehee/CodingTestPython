"""
프로그래머스: <모음 사전>

1. 아이디어:
    A E I O U 만을 조합하여 길이 5이하의 모든 단어 리스트 만들기
    단어를 입력했을 때 몇번째인지 인덱스 번호 출력
"""


def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    temp = []

    def dfs(cnt):
        if cnt == 1:
            word_list.append("".join(temp))
        if cnt == 2:
            word_list.append("".join(temp))
        if cnt == 3:
            word_list.append("".join(temp))
        if cnt == 4:
            word_list.append("".join(temp))
        if cnt == 5:
            word_list.append("".join(temp))
            return

        for i in range(5):
            temp.append(words[i])
            dfs(cnt + 1)
            temp.pop()

    dfs(0)
    print(word_list.index(word) + 1)


data = input()
solution(data)