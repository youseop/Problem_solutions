import sys
sys.stdin = open('input.txt', 'rt')
sys.setrecursionlimit(100000000)
n, k = map(int, sys.stdin.readline().split())

num = dict()
num[1] = 1


def func(a):
    if a in num:
        return num[a]
    else:
        num[a] = (func(a-1)*a)
        return num[a]


answer = func(n)//(func(k)*func(n-k))
print(answer % 1000000007)
