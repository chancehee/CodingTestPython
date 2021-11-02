'''
프로그래머스(level1): <모의고사>
'''
answer = [1,2,3,4,5]


def solution(answers):
    answer = []
    answer_temp = []
    count_a = 0
    count_b = 0
    count_c = 0
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    target = [A, B, C]
    idx_a, idx_b, idx_c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == A[i % len(A)]:
            count_a += 1
        if answers[i] == B[i % len(B)]:
            count_b += 1
        if answers[i] == C[i % len(C)]:
            count_c += 1

    answer_temp = [count_a, count_b, count_c]

    m = max(answer_temp)

    for i in range(3):
        if m == answer_temp[i]:
            answer.append(i + 1)
    return answer
print(solution(answer))

