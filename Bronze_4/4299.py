# 4299번 AFC 윔블던
import sys

def input():
    return sys.stdin.readline().rstrip()

plus, minus = map(int, input().split())

if (plus+minus) < 0 or (plus-minus) < 0 or (plus+minus) % 2 != 0:
    print(-1)
else:
    a = (plus+minus) // 2
    b = plus - a
    print(max(a, b), min(a, b))


