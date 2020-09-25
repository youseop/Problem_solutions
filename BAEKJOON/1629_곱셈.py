import sys
sys.stdin = open('input.txt', 'rt')

a, b, c = map(int, sys.stdin.readline().split())

num = dict()
num[1] = a % c


def mul(a, b):
    if b in num:
        return num[b]
    else:
        num[b] = (mul(a, b//2)*mul(a, b-b//2)) % c
        return num[b]


mul(a, b)
print(num[b])
