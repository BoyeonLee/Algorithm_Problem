# 15726번 이칙연산
# 한 번의 곱셈 기호와 한 번의 나눗셈 기호를 이용하여 만든 식 중 가장 큰 값을 출력
# 답은 int범위를 벗어나지 않는다.
# 소수점 아래는 버린다.

import sys, math

def input():
    return sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

print(math.floor(max( a * b / c, a / b * c)))
