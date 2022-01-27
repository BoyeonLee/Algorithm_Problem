# 1864번 문어 숫자
# -는 0에 대응한다.
# \는 1에 대응한다.
# (는 2에 대응한다.
# @는 3에 대응한다.
# ?는 4에 대응한다.
# >는 5에 대응한다.
# &는 6에 대응한다.
# %는 7에 대응한다.
# /는 -1에 대응한다.
# 문어 숫자를 입력 받아 십진수로 나타내는 것
# 입력으로 '#'이 들어오면 입력을 종료한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

dic = {'/':-1, '-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7}

li = []
while True:
    str_8 = input()
    num = 0
    if str_8 == '#':
        break
    str_8 = list(str_8)

    for i in range(len(str_8)):
        if str_8[i] in dic:
            dou = len(str_8) - 1 - i
            num += dic[str_8[i]]*(8**dou)
    li.append(num)

for i in li:
    print(i)

