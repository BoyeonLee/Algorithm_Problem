# 2355번 시그마

import sys

def input():
    return sys.stdin.readline().rstrip()

a,b = map(int, input().split())
if (b-a)%2 == 1:
    print( (a+b) * ((abs(b-a) + 1) // 2) )
else:
    print( ((a+b)//2) * (abs(b-a)+1) )