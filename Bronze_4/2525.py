# 2525번 오븐 시계

import sys

def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())
c = int(input())

if (b + c) >= 60:
    hour = a + (b+c) // 60
    minute = (b+c) % 60
else:
    hour = a
    minute = b+c

if hour >= 24:
    hour = hour - 24

print(hour, minute)