# 3052번 나머지

import sys

def input():
    return sys.stdin.readline().rstrip()

dic = {}
for _ in range(10):
    num = int(input())
    rem = num % 42
    if rem in dic:
        dic[rem] += 1
    else:
        dic[rem] = 1

print(len(dic))