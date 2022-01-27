# 1075번 나누기

# input으로 입력받은 n(현재 문자열)의 가장 뒷 두 자리를 0으로 만든 후
# 숫자로 변환(int_n)한다.
# int_n % f == 0이면 print(00)
# 아니면 결과물이 10보다 작을 때 클 때 나누고 
# 10보다 작으면 앞에 0 붙여서 출력

import sys

def input():
    return sys.stdin.readline().rstrip()

n = list(input())
f = int(input())

n[-1] = n[-2] = '0'
int_n = int(''.join(n))

if int_n % f == 0:
    print('00')
else:
    a = int_n // f
    re = f * (a+1) - int_n
    if re < 10:
        print(str(re).zfill(2))
    else:
        print(re)

