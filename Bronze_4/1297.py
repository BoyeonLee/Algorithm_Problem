import sys
import math

def input():
    return sys.stdin.readline().rstrip()

d,h,w = map(int, input().split())

r = math.sqrt(d**2/(h**2 + w**2))

height = math.floor(r*h)
width = math.floor(r*w)

print(height, width)