# 1159번 농구 경기

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
names = {}
for _ in range(n):
    name = input()[0]
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

result = []
for key, value in names.items():
    if value >= 5:
        result.append(key)
        
if result:
    result = sorted(result)
    print(''.join(result))
else:
    print('PREDAJA')