# 1964번 오각형, 오각형, 오각형...

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

points = 5
for i in range(2, n+1):
    points += 3*i + 1

print(points % 45678)