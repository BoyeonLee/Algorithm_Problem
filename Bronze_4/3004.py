# 3004번 체스판 조각
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = n//2 + 1

if n % 2 == 0:
    print(a**2)
else:
    print(a*(a+1))