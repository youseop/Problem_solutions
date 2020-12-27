import heapq as hq
from collections import deque
import sys
read = sys.stdin.readline

m, n = map(int, read().split())
maiz = list(list(read().strip()) for _ in range(n))
check = list(list(-1 for _ in range(m)) for _ in range(n))
check[0][0] = 0

point = [[0, 0, 0]]
hq.heapify(point)

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

while point:
    wall, a, b = hq.heappop(point)
    for x, y in zip(dx, dy):
        ax, by = a+x, b+y
        if 0 <= ax < n and 0 <= by < m and check[ax][by] == -1:
            if maiz[ax][by] == '1':
                hq.heappush(point, [wall+1, ax, by])
                check[ax][by] = wall+1
            else:
                hq.heappush(point, [wall, ax, by])
                check[ax][by] = wall
print(check[-1][-1])


##########################12-27-2020#####################################
import sys
read=sys.stdin.readline
import heapq as hq

dx = [1,0,0,-1]
dy=[0,1,-1,0 ]

m,n = map(int,read().split())
MAP = list(list( int(i) for i in list(read().strip())) for _ in range(n))
MAP[0][0] = -1
point = [(0,0,0)]

while point:
    
    break_wall, a, b = hq.heappop(point)
    if a == n-1 and b == m-1: 
        print(break_wall)
        break
    for x,y in zip(dx,dy):
        ax, by = a+x, b+y
        if 0<=ax<n and 0<=by<m and MAP[ax][by] != -1:
            if MAP[ax][by]:
                hq.heappush(point,(break_wall+1, ax, by))
            else:
                hq.heappush(point,(break_wall, ax, by))
            MAP[ax][by] = -1