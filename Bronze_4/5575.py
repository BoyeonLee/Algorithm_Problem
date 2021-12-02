# 5575번 타임카드

import sys

def input():
    return sys.stdin.readline().rstrip()

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_work = (a[3]*3600 + a[4]*60 + a[5]) - (a[0]*3600 + a[1]*60 + a[2])
b_work = (b[3]*3600 + b[4]*60 + b[5]) - (b[0]*3600 + b[1]*60 + b[2])
c_work = (c[3]*3600 + c[4]*60 + c[5]) - (c[0]*3600 + c[1]*60 + c[2])

total_work = [a_work, b_work, c_work]

for i in total_work:
    h = i // 3600
    m = (i%3600)//60
    s = (i%3600)%60
    print(h, m, s)