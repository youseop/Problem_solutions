import sys
from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    a = []
    for i in tmp:
        a.append(int(i))
    maze.append(a)
check = list(list(0 for _ in range(m)) for _ in range(n))
check[0][0] = 1

bfs = deque([[0, 0]])  # 너비 탐색을 위한 큐 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while bfs:
    tmp = bfs.popleft()
    if tmp == [n-1, m-1]:
        print(check[-1][-1])
        sys.exit()
    for x, y in zip(dx, dy):
        ax = tmp[0]+x
        by = tmp[1]+y
        if 0 <= ax < n and 0 <= by < m and check[ax][by] == 0 and maze[ax][by] != 0:
            check[ax][by] = check[tmp[0]][tmp[1]]+1
            bfs.append([ax, by])
