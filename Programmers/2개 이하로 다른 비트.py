#LV2 프로그래머스 레벨 테스트 오답 !!!
#문제: 주어진 숫자에서 비트가 2개 이하로 바뀌고 다음 가장 작은수 구하기
#아이디어: 숫자의 규칙을 느끼고 짝수일때는 +1 해주고 홀 수 일때는 LSB에서 가장 가까운 0비트를 1로 바꾸고 다음 비트를 1로 바꿔준다.
#내가 부족한 부분(공부해야할 부분): join함수 활용: "구분자".join() / rfind():인덱스 위치알려준다 / bin() / int(a,2) / list(문자열)

def solution(numbers):
    answer=[]

    for number in numbers:
        if number%2 == 0: #짝수일 경우
            binary_num = list(bin(number)[2:])
            binary_num[-1] = "1"
        else: #홀수일 경우
            binary_num = bin(number)[2:]
            binary_num = "0" + binary_num
            one_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[one_idx] = "1"
            binary_num[one_idx+1] = "0"

        ans_num = int("".join(binary_num),2)
        answer.append(ans_num)

    return answer

print(solution([6,8,10,120,7,9,11,15]))