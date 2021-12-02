# 5596번 시험점수
# 민국이와 만세가 본 4과목의 점수를 입력하면, 민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력.
# 단, 서로 동점일 때는 민국이의 총점 S를 출력한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

min = list(map(int, input().split()))
man = list(map(int, input().split()))

if sum(min) == sum(man):
    print(sum(min))
else:
    print(max(sum(min), sum(man)))
