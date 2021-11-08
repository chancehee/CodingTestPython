'''
문자열: <크로아티아 알파벳>
'''

cro = ['dz=','c=','c-','d-','lj','nj','s=','z=']

word = 'dz=ak'

for c in cro:
    word = word.replace(c,'*')

print(len(word))
