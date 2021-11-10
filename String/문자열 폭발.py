'''
문자열: <문자열 폭발>
'''

data = "12ab112ab2ab"
target = "12ab"

a = []
for i in data:
    a.append(i)

    if len(a) >= len(target):

        # 끝에 target 길이만큼 비교
        if a[len(a)-len(target):] == list(target):
            del a[len(a)-len(target):]

if a:
    print("".join(a))
else:
    print("FRULA")














