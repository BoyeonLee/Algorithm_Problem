# 1598번 꼬리를 무는 숫자 나열

import sys

def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())

a1 = a // 4 # a를 4로 나눈 몫
a2 = a % 4
b1 = b // 4
b2 = b % 4

if a2 == 0: 
    a2 = 4
    a1 -= 1
if b2 == 0: 
    b2 = 4
    b1 -= 1

print(abs(b1 - a1) + abs(b2 - a2))
