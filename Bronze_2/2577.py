# 2577번 숫자의 개수

import sys

def input():
    return sys.stdin.readline().rstrip()

total = 1
for _ in range(3):
    num = int(input())
    total *= num

key = [0,1,2,3,4,5,6,7,8,9]
dic = {}
for i in key:
    dic[i] = 0

for i in str(total):
    dic[int(i)] += 1

for value in dic.values():
    print(value)

