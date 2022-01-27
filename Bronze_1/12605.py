# 12605번 단어순서 뒤집기

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

sens = []
for _ in range(n):
    sens.append(input())

ans = []
for sen in sens:
    ans.append(sen.split()[::-1])

for i in range(len(ans)):
    print(f"Case #{i+1}:", ' '.join(ans[i]))
