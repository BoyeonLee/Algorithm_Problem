# 1267번 핸드폰 요금
# 영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 
# 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.
# 민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 
# 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.
# 첫째 줄에 싼 요금제의 이름을 출력한다. 그 후에 공백을 사이에 두고 요금이 몇 원 나오는지 출력한다. 
# 만약 두 요금제의 요금이 모두 같으면 영식을 먼저 쓰고 민식을 그 다음에 쓴다.
# 영식은 Y로, 민식은 M으로 출력한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
times = list(map(int, input().split()))

yprice = 0
mprice = 0
for i in times:
    y_mul = i // 30
    m_mul = i // 60

    yprice += 10 * (1 + y_mul)
    mprice += 15 * (1 + m_mul)

if yprice == mprice:
    print("Y M", yprice)
elif yprice > mprice:
    print("M", mprice)
else:
    print("Y", yprice)
