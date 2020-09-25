import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())


def m_fibo(x, n):
    if len(fibo) > x:
        return fibo[x]
    else:
        fibo[x] = (m_fibo(x-1, n)+m_fibo(x-2, n)) % n
        return fibo[x]


def mode(n):
    x = 1
    while True:
        if fibo[x] == 0 and fibo[x-1] == 1:
            return x
        x += 1
        m_fibo(x, n)


for _ in range(n):
    fibo = dict()
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    a, n = map(int, sys.stdin.readline().split())
    print(a, mode(n))
