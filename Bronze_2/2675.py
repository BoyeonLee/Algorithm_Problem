# 2675번 문자열 반복

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

tog = []
for _ in range(n):
    num, word = input().split()
    tog.append((int(num), word))

for i in tog:
    result = ''
    for j in list(i[1]):
        result += j * i[0]
    print(result)