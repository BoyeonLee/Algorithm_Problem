# 1100번 하얀 칸

# 체스판은 8×8크기, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 
# 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# chess[i][j] 한 칸
# 흰 칸은 i=짝수, j=짝수 이거나 i=홀수, j=홀수

import sys

def input():
    return sys.stdin.readline().rstrip()

chess = []

for _ in range(8):
    chess.append(input())

cnt = 0
for i in range(8):
    for j in range(8):
        if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 == 1) and (j % 2 == 1)):
            if chess[i][j] == 'F':
                cnt += 1

print(cnt)
