# 17608번 막대기
# 단순히 마지막 막대기랑만 비교할 게 아니고, 끝에서부터 비교하면서 큰 막대가 나타나면 max 바꿔주기

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
sticks = []
for _ in range(n):
    sticks.append(int(input()))

cnt = 1
max = sticks[-1]
for i in range(len(sticks)-1, -1, -1):
    if sticks[i] > max:
        cnt += 1
        max = sticks[i]

print(cnt)