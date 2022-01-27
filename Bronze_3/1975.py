# 1975번 Number Game

import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def restZero(a, b, cnt):
    if a != 0 and a % b == 0:
        cnt += 1
        return restZero(a//b, b, cnt)
    else:
        return cnt

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))

ans = []
for i in li:
    sums = 0
    for j in range(2, i+1):
        cnt = restZero(i, j, 0)
        sums += cnt
    ans.append(sums)

for i in ans:
    print(i)