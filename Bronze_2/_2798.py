# 2798번 블랙잭
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
kards = sorted(list(map(int, input().split())))

result = 0
for i in range(len(kards)):
    for j in range(i+1, len(kards)):
        for k in range(j+1, len(kards)):
            if kards[i] + kards[j] + kards[k] <= m:
                result = max(result, kards[i] + kards[j] + kards[k])
            else:
                continue

print(result)

