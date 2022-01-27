# 1703번 생장점

import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    leaves = list(map(int, input().split()))

    if leaves[0] == 0:
        break

    n = 1
    for i in range(leaves[0]):
        sf = leaves[2*i + 1]
        p = leaves[2*i + 2]
        n = n*sf - p

    print(n)