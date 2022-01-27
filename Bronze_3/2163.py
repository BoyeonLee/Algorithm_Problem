# 2163번 초콜릿 자르기

import sys

def input():
    return sys.stdin.readline().rstrip()

n,m = map(int, input().split())

if n > 1 or m > 1:
    print(n * m - 1)
else:
    print(0)