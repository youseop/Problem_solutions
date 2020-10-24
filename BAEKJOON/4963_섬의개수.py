from collections import deque
import sys
read = sys.stdin.readline


def BFS(MAP, w, h):
    answer = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                point = deque([[i, j]])
                while point:
                    a, b = point.popleft()
                    for x, y in zip(dx, dy):
                        ax, by = a+x, b+y
                        if 0 <= ax < h and 0 <= by < w and MAP[ax][by] == 1:
                            point.append([ax, by])
                            MAP[ax][by] = -1
                answer += 1
    return answer


dx = [1, 0, 0, -1, 1, 1, -1, -1]
dy = [0, 1, -1, 0, -1, 1, -1, 1]

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    MAP = list(list(map(int, read().split())) for _ in range(h))

    print(BFS(MAP, w, h))

    # for M in MAP:
    #    print(*M)
    # print()
