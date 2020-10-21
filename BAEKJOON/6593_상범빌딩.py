from collections import deque
import sys
sys.stdin = open("input.txt", "rt")
read = sys.stdin.readline

dx = [0, 0, 1, 0, 0, -1]
dy = [0, 1, 0, 0, -1, 0]
dz = [1, 0, 0, -1, 0, 0]

while True:
    l, r, c = map(int, read().split())
    if l == 0 and r == 0 and c == 0:
        break
    B = []
    for _ in range(l):
        tmp = list(list(read().strip()) for _ in range(r))
        B.append(tmp)
        tmp = read()
    point = deque([])
    end_point = []
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if B[k][i][j] == 'S':
                    point.append([k, i, j])
                    B[k][i][j] = 0
                elif B[k][i][j] == 'E':
                    end_point = [k, i, j]
                    B[k][i][j] = '.'
    flag = 2
    while point:
        if flag == 1:
            break
        a, b, q = point.popleft()
        for x, y, z in zip(dx, dy, dz):
            ax, by, qz = a+x, b+y, q+z
            if 0 <= ax < l and 0 <= by < r and 0 <= qz < c and B[ax][by][qz] == ".":
                point.append([ax, by, qz])
                B[ax][by][qz] = B[a][b][q]+1
                if [ax, by, qz] == end_point:
                    print('Escaped in ', B[ax][by][qz], ' minute(s).', sep="")
                    flag = 1

    if flag == 2:
        print('Trapped!')
