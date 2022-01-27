# 1145번 적어도 대부분의 배수
# 5개의 자연수 중에서 최소 3개로 나눠지는 가장 작은 자연수 구하기

# 못 풀어서 검색해봄...

# 리스트 중 가장 작은 수(n)를 지정하고 그 수를 리스트에 있는 모든 숫자로 나눠본 후
# cnt <= 3 이라면 n에 1을 더한다.
# cnt >= 3 일때까지 반복. 

import sys

def input():
    return sys.stdin.readline().rstrip()

arr = list(map(int, input().split()))
n = min(arr)

while True:
    cnt = 0
    for i in arr:
        if n % i == 0:
            cnt += 1
        
    if cnt > 2:
        print(n)
        break
    n += 1

