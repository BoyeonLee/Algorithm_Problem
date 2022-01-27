# 1152번 단어의 개수
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
# 이 문자열에는 몇 개의 단어가 있을까? 

import sys

def input():
    return sys.stdin.readline().rstrip()

str_list = list(input().split())

print(len(str_list))