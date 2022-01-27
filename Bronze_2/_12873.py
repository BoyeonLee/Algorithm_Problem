# 12873번 기념품

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

'''
1. 참가자 인원의 티셔츠 번호를 큐에 담아서 큐로 처리한다.
2. 참가자 인원 - 1 만큼 게임을 진행할 수 있게 반복처리한다.
3. 탈락자는 단계의 세제곱 % 참가자 수를 큐 순서에 대입해서 탈락자를 정한다.
4. 탈락자는 dequeue하기 위해 맨 앞에 와있어야한다.(티셔츠 번호가 담긴 큐의 순서를 조정해야함)
5. 탈락자가 발생할 때마다 단계를 한단계씩 높이고 다시 게임을 진행한다.
6. 게임이 끝나면 남아있는 티셔츠 번호를 출력한다.
7. 예외) 탈락자를 구하는 나머지가 1인 경우 큐의 순서를 조정할 필요가 없다.
'''

n = int(input())
que = deque([i for i in range(1, n+1)])

num = 2
while len(que) > 1:
    que.popleft()
    idx = pow(num,3) % len(que) - 1
    que.rotate(-idx)
    num += 1

print(que[0])
        