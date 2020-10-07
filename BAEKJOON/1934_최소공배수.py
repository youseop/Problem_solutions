import sys


def GCF(x, y):
    while(y):
        x, y = y, x % y
    return x


for _ in range(int(input())):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.sort()
    a = tmp[0]
    b = tmp[1]
    gcf = GCF(a, b)
    print(a*b//gcf)
