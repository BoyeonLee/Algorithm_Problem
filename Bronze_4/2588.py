# 2588번 곱셈

import sys

def input():
    return sys.stdin.readline().rstrip()

a = list(input())
b = list(input())

num_list = []
for i in b:
    num = int(''.join(a)) * int(i)
    num_list.append(num)

num_list.reverse()
result = int(''.join(a)) * int(''.join(b))
num_list.append(result)

for i in num_list:
    print(i)
