from copy import deepcopy
from collections import deque as dq
import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000000000)
n, m = map(int, read().split())

lab = list(list(map(int, read().split())) for _ in range(n))
two = []
not_zero = 3
for i in range(n):
    for j in range(m):
        if lab[i][j] == 1:
            not_zero += 1
        if lab[i][j] == 2:
            two.append([i, j])
            not_zero += 1
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
answer = 0


def BFS():
    cnt = 0
    tmp_lab = [lab[i][::] for i in range(n)]
    tmp_two = dq(two[::])
    while tmp_two:
        a, b = tmp_two.popleft()
        for x, y in zip(dx, dy):
            ax, by = a+x, b+y
            if 0 <= ax < n and 0 <= by < m and tmp_lab[ax][by] == 0:
                tmp_lab[ax][by] = 2
                cnt += 1
                if answer > n*m-cnt-not_zero:
                    return 2147000000
                tmp_two.append([ax, by])
    return cnt


def WALL(a, b, cnt):
    global answer
    if cnt == 3:
        safe = n*m-BFS()-not_zero
        answer = max(answer, safe)
        return
    if a == n:
        return
    flag = 1
    if lab[a][b] == 0:
        lab[a][b] = 1
        if b == m-1:
            WALL(a+1, 0, cnt+1)
            lab[a][b] = 0
            WALL(a+1, 0, cnt)
        else:
            WALL(a, b+1, cnt+1)
            lab[a][b] = 0
            WALL(a, b+1, cnt)
    else:
        if b == m-1:
            WALL(a+1, 0, cnt)
        else:
            WALL(a, b+1, cnt)


WALL(0, 0, 0)
print(answer)
