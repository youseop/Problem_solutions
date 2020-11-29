import sys
read = sys.stdin.readline

n, m = map(int, read().split())
MAP = list(list(map(int, read().split())) for _ in range(n))

CCTV = list()
n_cctv = 0
WALL = list()
count = n*m

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 6:
            WALL.append((i, j))
            count -= 1
        elif MAP[i][j] > 0:
            CCTV.append((MAP[i][j], i, j))
            n_cctv += 1
            count -= 1


def one(direction, a, b):
    point = [0]
    if direction == 0:
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    return point
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
    if direction == 1:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    return point
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
    if direction == 2:
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    return point
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 3:
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    return point
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    return point


def two(direction, a, b):
    point = [0]
    if direction == 0:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
    if direction == 1:
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    return point


def three(direction, a, b):
    point = [0]
    if direction == 0:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 1:
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 2:
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 3:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    return point


def four(direction, a, b):
    point = [0]
    if direction == 0:
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break

    if direction == 1:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 2:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    if direction == 3:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
    return point


def five(direction, a, b):
    point = [0]
    if direction == 0:
        for i in range(n):
            ai = a-i
            if ai >= 0:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b+i
            if bi < m:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
        for i in range(n):
            ai = a+i
            if ai < n:
                if MAP[ai][b] == 6:
                    break
                elif MAP[ai][b] == 0:
                    point[0] += 1
                    point.append([ai, b])
                else:
                    continue
            else:
                break
        for i in range(m):
            bi = b-i
            if bi >= 0:
                if MAP[a][bi] == 6:
                    break
                elif MAP[a][bi] == 0:
                    point[0] += 1
                    point.append([a, bi])
                else:
                    continue
            else:
                break
    return point


def DFS(index):
    global count, answer
    if index == n_cctv:
        answer = min(answer, count)
        return
    t, a, b = CCTV[index]
    if t == 1:
        for i in range(4):
            point = one(i, a, b)
            count -= point[0]
            for x, y in point[1:]:
                MAP[x][y] = -1
            DFS(index+1)
            count += point[0]
            for x, y in point[1:]:
                MAP[x][y] = 0
    elif t == 2:
        for i in range(2):
            point = two(i, a, b)
            count -= point[0]
            for x, y in point[1:]:
                MAP[x][y] = -1
            DFS(index+1)
            count += point[0]
            for x, y in point[1:]:
                MAP[x][y] = 0
    if t == 3:
        for i in range(4):
            point = three(i, a, b)
            count -= point[0]
            for x, y in point[1:]:
                MAP[x][y] = -1
            DFS(index+1)
            count += point[0]
            for x, y in point[1:]:
                MAP[x][y] = 0
    if t == 4:
        for i in range(4):
            point = four(i, a, b)
            count -= point[0]
            for x, y in point[1:]:
                MAP[x][y] = -1
            DFS(index+1)
            count += point[0]
            for x, y in point[1:]:
                MAP[x][y] = 0
    if t == 5:
        for i in range(1):
            point = five(i, a, b)
            count -= point[0]
            for x, y in point[1:]:
                MAP[x][y] = -1
            DFS(index+1)
            count += point[0]
            for x, y in point[1:]:
                MAP[x][y] = 0


answer = sys.maxsize
DFS(0)
print(answer)
