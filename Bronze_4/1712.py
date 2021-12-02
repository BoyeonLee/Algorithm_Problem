import sys

def input():
    return sys.stdin.readline().rstrip()

a,b,c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)) + 1)

# if문으로 먼저 걸러줘야 시간을 단축할 수 있다.