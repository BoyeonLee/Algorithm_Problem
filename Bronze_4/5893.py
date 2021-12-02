# 5893번 17배
# 이진수 N이 입력으로 들어오면 17을 곱한 다음 이진수로 출력

import sys

def input():
    return sys.stdin.readline().rstrip()

a = input()
print( bin(int(a, 2) * 17)[2:] )
