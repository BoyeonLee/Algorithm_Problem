# 2562번 최댓값

import sys

def input():
    return sys.stdin.readline().rstrip()

max = 0
loc = 0
for i in range(1, 10):
    num = int(input())
    if num > max:
        max = num
        loc = i

print(max)
print(loc)