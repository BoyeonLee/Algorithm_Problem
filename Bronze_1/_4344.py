# 4344번 평균은 넘겠지

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

result = []
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    cnt = 0
    for i in nums[1:]:
        if i > avg:
            cnt += 1
    rate = cnt / nums[0] * 100
    print(f'{rate:.3f}%')


    
