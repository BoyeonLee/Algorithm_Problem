# 2752번 세수정렬
import sys

def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()
for i in l:
    print(i, end=' ')

