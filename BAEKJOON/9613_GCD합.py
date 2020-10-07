import sys
import itertools


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


for _ in range(int(input())):
    numbs = list(map(int, sys.stdin.readline().split()))[1:]

    combs = list(itertools.combinations(numbs, 2))
    sum = 0
    for comb in combs:
        sum += GCD(comb[0], comb[1])
    print(sum)
