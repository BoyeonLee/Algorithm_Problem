# 2161번 카드1

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
que = deque([i for i in range(1, n+1)])
dump = []

while len(que) > 1:
    d = que.popleft()
    dump.append(d)
    que.rotate(-1)
dump.append(que[0])

for i in dump:
    print(i, end=' ')
