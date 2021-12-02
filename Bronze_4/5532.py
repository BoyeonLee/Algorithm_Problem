# 5532번 방학 숙제

import sys

def input():
    return sys.stdin.readline().rstrip()

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

kor = a//c if a % c == 0 else (a//c) + 1
math = b//d if b % d == 0 else (b//d) + 1

if kor >= math:
    print(l - kor)
else:
    print(l - math)