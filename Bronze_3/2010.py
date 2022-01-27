# 2010번 플러그

import sys

def input():
    return sys.stdin.readline().rstrip()

cnt = 0
n = int(input())
for i in range(n):
    if i == n-1:
        cnt += int(input())
    else:
        cnt += int(input()) - 1

print(cnt)