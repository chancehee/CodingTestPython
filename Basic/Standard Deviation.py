'''
1.일반적인 계산식

2.Numpy

'''

import math

'''
vals = [i+1 for i in range(10)]

mean = sum(vals) / len(vals)

vsum = 0
for val in vals:
    vsum = vsum + (val - mean)**2 #** 거듭제곱

variance = vsum / len(vals)
print(variance) #분산

std = math.sqrt(variance)
print(std)
'''

def std_value(a):
    m = sum(a) / len(a)
    s =0
    for i in a:
        s = s + (i-m)**2
    vari = s/len(a)
    std = math.sqrt(vari)
    return std

def find_list(a):




