import sys
read = sys.stdin.readline


def LCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x


for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))
    num.sort()

    diff = set()
    for i in range(1, n):
        diff.add(num[i]-num[i-1])
    if diff == {0}:
        print('INFINITY')
        continue
    diff = list(diff)
    x = diff[0]
    for i in range(1, len(diff)):
        tmp = LCD(x, diff[i])
        x = tmp
    print(x)
