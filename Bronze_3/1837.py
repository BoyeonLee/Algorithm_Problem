# 1837번 암호제작
# 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호 => 두 소수 모두 k보다 크면 좋은 암호
# 좋은 암호이면 첫째 줄에 GOOD을 출력하고, 
# 만약에 좋지 않은 암호이면 BAD와 소수 r을 공백으로 구분하여 출력하는데 r은 작은 소수를 의미한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

p, k = map(int, input().split())

bad = 0
for i in range(2, k):
    if p % i == 0:
        print('BAD', i)
        bad = 1
        break

if bad == 0:
    print('GOOD')