# 1547번 공

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cups = [1, 2, 3]

for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue
    a_idx = cups.index(a)
    b_idx = cups.index(b)
    cups[a_idx] = b
    cups[b_idx] = a

print(cups[0])
