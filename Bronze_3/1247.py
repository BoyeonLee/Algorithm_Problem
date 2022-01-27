# 1247번 부호

# 총 3개의 데이터 셋
# 첫째 줄은 N(1 ≤ N ≤ 100,000)
# 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다.
# 각 테스트 셋에 대해 N개의 정수들의 합 S의 부호 출력
#  S=0이면 "0"을, S>0이면 "+"를, S<0이면 "-"를 출력하면 된다.

import sys

def input():
    return sys.stdin.readline().rstrip()

n_list = []
num_list = [[] * i for i in range(3)]
sum_list = []

for i in range(3):
    n = int(input())
    for _ in range(n):
        num_list[i].append(int(input()))
    sum_list.append(sum(num_list[i]))

for i in range(3):
    if sum_list[i] == 0:
        print('0')  
    elif sum_list[i] > 0:
        print('+')
    elif sum_list[i] < 0:
        print('-')  
