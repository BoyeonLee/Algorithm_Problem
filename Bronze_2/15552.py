# 15552번 빠른 A + B

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = []
for _ in range(n):
    num1, num2 = map(int, input().split())
    result.append(num1 + num2)

for i in result:
    print(i)