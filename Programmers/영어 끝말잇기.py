'''
프로그래머스(level2): <영어 끝말잇기>
'''

n = 3
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#3번 사람이 3번째 말한 단어에서 틀렸다. result= [3,3]
def solution(n, words):
    sayed = set()
    result = [0, 0]
    for i, w in enumerate(words):
        if w in sayed:
            result[0] = (i % n + 1)
            result[1] = (i // n + 1)
            return result
        elif i < len(words) - 1:
            if words[i + 1][0] != w[-1]:
                result[0] = ((i + 1) % n + 1)
                result[1] = ((i + 1) // n + 1)
                return result

        sayed.add(w)
    return result

print(solution(n,words))
