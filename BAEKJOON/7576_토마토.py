from collections import deque
import sys
read = sys.stdin.readline


n, m = map(int, read().split())
tom = list(list(map(int, read().split())) for _ in range(m))

check = list(list(-1 for _ in range(n)) for _ in range(m))
point = deque([])

for i in range(m):
    for j in range(n):
        if tom[i][j] == 1:
            point.append([i, j])
            check[i][j] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while point:
    a, b = point.popleft()
    for x, y in zip(dx, dy):
        ax = a+x
        by = b+y
        if 0 <= ax < m and 0 <= by < n and tom[ax][by] == 0:
            if check[ax][by] == -1:
                check[ax][by] = check[a][b]+1
            else:
                check[ax][by] = min(check[ax][by], check[a][b]+1)
            tom[ax][by] = 1
            point.append([ax, by])

for aa in tom:
    if 0 in aa:
        print(-1)
        sys.exit()

answer = 0
for i in range(m):
    answer = max(answer, max(check[i]))
print(answer)
