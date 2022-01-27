# 1546번 평균

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
scores = list(map(int, input().split()))
max = max(scores)

print(sum(scores) / max * 100 / n)