import sys

def input():
    return sys.stdin.readline().rstrip()

a,b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')