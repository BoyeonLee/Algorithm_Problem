# 2292번 벌집

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cnt = 1
total = 1
while n > total:
    total += cnt * 6
    cnt += 1

print(cnt)