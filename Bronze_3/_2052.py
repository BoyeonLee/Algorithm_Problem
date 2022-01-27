# 2052번 지수연산
# 실패
# python은 소수점 아래 숫자가 많아지면 e로 표현한다. 이 부분을 숫자로 풀어줘야 되는 문제였다.

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
result = "%.250f" %(2**(-n)) # 소수점 아래 250자리까지 표시하겠다.
last = len(result)
for i in range(last-1,1,-1):
    if result[i] != "0":
        last = i
        break

print(result[:last+1])