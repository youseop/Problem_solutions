import sys
read = sys.stdin.readline

n, m = map(int, read().split())
root = list(i for i in range(n+1))


def find_root(x):
    if x == root[x]:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]


def union(x, y):
    a = find_root(x)
    b = find_root(y)
    if a != b:
        root[b] = a


for _ in range(m):
    op, a, b = map(int, read().split())
    if op == 0:
        union(a, b)
    else:
        if find_root(a) == find_root(b):
            print('YES')
        else:
            print("NO")
