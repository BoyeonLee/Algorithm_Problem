# 15873번 공백 없는 A+B
# 자연수 A, B (0 < A, B ≤ 10)
# 두 수의 사이에는 공백이 주어지지 않는다. 
# 두 수의 앞에 불필요한 0이 붙는 경우는 없다.

import sys

def input():
    return sys.stdin.readline().rstrip()

li = list(input())
li = list(map(int, li))

if len(li) < 3:
    print(li[0] + li[1])
elif len(li) == 3:
    if li[1] == 0:
        first = int(str(li[0]) + str(li[1]))
        print( first + li[2] )
    elif li[1] == 1:
        second = int(str(li[1]) + str(li[2]))
        print( li[0] + second )
elif len(li) == 4:
    print(20)
