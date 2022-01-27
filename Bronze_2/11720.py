# 11720번 숫자의 합

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

nums = input()
print( sum(map(int, list(nums))) )