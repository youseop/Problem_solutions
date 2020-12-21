import sys
read=sys.stdin.readline
from collections import deque

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def next_fish(start):
    far = 0
    check = list(list(True for _ in range(n)) for _ in range(n))
    check[start[0]][start[1]] = False
    point = deque([start])
    while point:
        point = deque(sorted(point))
        for _ in range(len(point)):
            a,b = point.popleft()
            if 0<MAP[a][b]<shark_size: 
                MAP[a][b]=0
                return [a,b], far
            for x,y in zip(dx,dy):
                ax, by = a+x, b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by] <= shark_size and check[ax][by]:
                    point.append([ax,by])
                    check[ax][by] = False
        far += 1
    return 0, 0

n = int(read())
MAP = list(list(map(int,read().split())) for _ in range(n))
time = 0
shark_size = 2
shark_exp = 0
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 9:
            start = [i,j]
            MAP[i][j] = 0

while True:
    start, tmp = next_fish(start)
    time += tmp
    if start:
        shark_exp += 1
        if shark_exp == shark_size:
            shark_size += 1
            shark_exp = 0
    else: 
        break
print(time)


