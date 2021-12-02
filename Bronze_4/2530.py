# 2530번 인공지능 시계

import sys

def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
d = int(input())

t_minute = a * 3600 + b * 60 + c + d

seconde = t_minute % 60
minute = (t_minute // 60) % 60
hour = t_minute // 3600

if hour >= 24:
    hour = hour % 24

print(hour, minute, seconde) 