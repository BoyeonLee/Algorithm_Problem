# 1076번 저항
import sys

def input():
    return sys.stdin.readline().rstrip()

dict = {'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9}

col1 = input()
col2 = input()
col3 = input()

if col1 in dict.keys():
    num1 = dict[col1] * 10
if col2 in dict.keys():
    num2 = dict[col2]
if col3 in dict.keys():
    mul = 10 ** dict[col3]

print( (num1 + num2) * mul)