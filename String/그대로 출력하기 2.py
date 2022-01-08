'''
문자열: <그대로 출력하기 2>
'''


while True:
    try:
        print(input())
    # End Of File
    except EOFError:
        break

