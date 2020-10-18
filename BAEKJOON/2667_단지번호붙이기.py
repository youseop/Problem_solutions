from collections import deque
import sys
read = sys.stdin.readline

n = int(read())

house = list(list(read().strip()) for _ in range(n))

sys.setrecursionlimit(1000000)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x):
    house_num = 1
    while save:
        a, b = save.popleft()

        for x, y in zip(dx, dy):
            ax = a+x
            by = b+y
            if 0 <= ax < n and 0 <= by < n and house[ax][by] == '1':
                save.append([ax, by])
                house[ax][by] = x
                house_num += 1

    return house_num


cnt = 0
answer = []
for i in range(n):
    for j in range(n):
        if house[i][j] == '1':
            save = deque([[i, j]])
            house[i][j] = cnt
            answer.append(bfs(cnt))
            cnt += 1

answer.sort()
print(cnt)
for a in answer:
    print(a)
print()
