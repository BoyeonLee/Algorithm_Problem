# 16428번 A/B - 3
# A = qB + r (0 ≤ r < |B|)로 나타낼 수 있을 때, q를 몫, r을 나머지
# 몫, 나머지 출력
# 1. A > 0, B > 0
# 2. A > 0, B < 0
# 3. A < 0, B > 0 
# 4. A < 0, B < 0

import sys

def input():
    return sys.stdin.readline().rstrip()

a, b = map(int, input().split())

if a > 0 and b < 0:
    quo = (a//b) + 1 # 몫
    print(quo)
    print(a - quo*b)
elif a < 0 and b < 0:
    print(a // b)
    print(abs(a % b))
else:
    print(a // b)
    print(a % b)