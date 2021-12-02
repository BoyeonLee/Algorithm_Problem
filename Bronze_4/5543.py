# 5543번 상근날드

import sys

def input():
    return sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
c = int(input())
coke = int(input())
cider = int(input())

print(min(a,b,c) + min(coke,cider) - 50)
