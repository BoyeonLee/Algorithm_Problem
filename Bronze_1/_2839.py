# 2839번 설탕 배달

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        sys.exit()
    else:
        n -= 3
        cnt += 1

print(-1)