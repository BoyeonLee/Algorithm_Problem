# 16466번 콘서트

import sys

def input():
    return sys.stdin.readline().rstrip()

'''
1 2 4 7 8
1 2 3 4 5

두 배열의 각 원소를 순서대로 비교해나간다.
서로 값이 다를 경우 해당 순서의 자리가 빈 것!
다른 값이 없을 경우 마지막 자리보다 한 자리 뒤가 답이다.
'''

n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
num_list = [i for i in range(1, n+1)]

for i,j in zip(nums, num_list):
    if i != j:
        print(j)
        sys.exit()

print(n+1)

