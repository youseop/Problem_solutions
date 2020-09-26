import math
n, m = map(int, input().split())


def five(a):
    if a == 0:
        return 0
    five = int(math.log(a)/math.log(5))
    sum = 0
    for i in range(1, five+1):
        sum += a//(5**i)
    return sum


def two(a):
    if a == 0:
        return 0
    two = int(math.log(a)/math.log(2))
    sum = 0
    for i in range(1, two+1):
        sum += a//(2**i)
    return sum


res = [five(n)-five(m)-five(n-m), two(n)-two(m)-two(n-m)]
print(min(res))
