# 15596번 정수 N개의 합

def solve(a):
    len_a = len(a)
    sums = 0
    if len_a % 2 == 1:
        for i in range(len_a//2):
            sums += a[i] + a[len_a-i-1]
        sums += a[len_a//2]
        return sums
    else:
        for i in range(len_a//2):
            sums += a[i] + a[len_a-i-1]
        return sums

solve([1,2,3,4,5])