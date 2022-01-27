# 1212번 8진수 2진수

# 8진수를 2진수로 변환
# 2진수로 바꿔주는 함수인 bin(x)을 이용
# x는 숫자여야 한다.
# 반환되는 건 문자열.

import sys

def input():
    return sys.stdin.readline().rstrip()


print(bin(int(input(), 8))[2:])