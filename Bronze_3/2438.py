# 2438번 별 찍기-1
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for i in range(1,n+1):
    print('*' * i)