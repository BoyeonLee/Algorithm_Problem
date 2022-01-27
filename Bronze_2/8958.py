# 8958번 OX퀴즈

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = []
for _ in range(n):
    x = None
    sums = 0
    for idx, a in enumerate(list(input())):
        if x == None and a == 'O':
            sums += (idx + 1)
        elif a == 'X':
            x = idx
        else:
            sums += (idx - x)
    result.append(sums)

for i in result:
    print(i)