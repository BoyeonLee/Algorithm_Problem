# 1284번 집 주소
# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

numbers = []
while True:
    n = input()
    if n == '0':
        break
    numbers.append(n)

for i in numbers:
    leng = 1 + len(i)
    for j in i:
        if j == '0':
            leng += 4
        elif j == '1':
            leng += 2
        else:
            leng += 3
    print(leng)