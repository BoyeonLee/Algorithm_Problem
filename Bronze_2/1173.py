# 1173번 운동

import sys

def input():
    return sys.stdin.readline().rstrip()

N, m, M, T, R = map(int, input().split())

time = 0
present = 0
while N > 0:
    if m+T <= M:
        time += 1
        N -= 1
        present = m+T
    else:

