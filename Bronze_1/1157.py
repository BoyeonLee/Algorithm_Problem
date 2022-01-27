# 1157번 단어공부
# 가장 많이 사용된 알파벳이 무엇인지
# 단, 대문자와 소문자를 구분하지 않는다.
# 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

char = list(input().upper())
dict = {}

for i in char:
    if i not in dict:
        dict[i] = 0
    else:
        dict[i] += 1

result = [k for k,v in dict.items() if max(dict.values()) == v]
if len(result) == 1:
    print(result[0])
else:
    print('?')
