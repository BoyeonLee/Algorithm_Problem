# 5622번 다이얼

import sys
import string

def input():
    return sys.stdin.readline().rstrip()

words = input()

alpha = list(string.ascii_uppercase)

result = 0
for i in words:
    idx = alpha.index(i)
    if i == 'S' or i == 'V' or i == 'Y' or i == 'Z':
        result += (idx // 3) + 2
    else:
        result += (idx // 3) + 3

print(result)