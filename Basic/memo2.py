from collections import deque

a = deque(maxlen=3)
print(a)
a.append(1)
a.append(2)
a.append(3)
print(a)
a.append(4)
print(a)

