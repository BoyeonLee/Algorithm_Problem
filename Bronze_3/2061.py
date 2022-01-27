# 2061번 좋은 암호

import sys

def input():
    return sys.stdin.readline().rstrip()

k,l = map(int, input().split())

result = 1
num = 0
for i in range(2, l):
    if k % i == 0:
        result = 0
        num = i
        break

if result == 1:
    print('GOOD')
else:
    print('BAD', num)