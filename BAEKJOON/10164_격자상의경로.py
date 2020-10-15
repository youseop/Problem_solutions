import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
k -= 1
point = [k//m, k % m]

cnt = 0


def dfs(a, b, c, d):
    global cnt
    if a == c and b == d:
        cnt += 1
        return
    for dx, dy in [[0, 1], [1, 0]]:
        da = a+dx
        db = b+dy
        if da <= c and db <= d:
            dfs(da, db, c, d)


if k == -1:
    dfs(0, 0, n-1, m-1)
    print(cnt)
else:
    dfs(0, 0, point[0], point[1])
    tmp1 = cnt
    cnt = 0
    dfs(point[0], point[1], n-1, m-1)
    tmp2 = cnt
    print(tmp1*tmp2)
