# 10809번 알파벳 찾기

import sys
import string

def input():
    return sys.stdin.readline().rstrip()

word = input()
for i in string.ascii_lowercase:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')