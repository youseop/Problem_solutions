import itertools
n, m = map(int, input().split())
numb = list(map(int, input().split()))
numb.sort()
tmp = list(itertools.combinations_with_replacement(numb, m))
for x in tmp:
    print(*x)
