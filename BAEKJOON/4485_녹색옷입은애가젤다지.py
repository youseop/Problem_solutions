import heapq as hq
from collections import deque
import sys
read = sys.stdin.readline

inf = sys.maxsize
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
i = 0

while True:
    i += 1
    n = int(read())
    if n == 0:
        break
    MAP = list(list(map(int, read().split())) for _ in range(n))
    dp = list(list(inf for _ in range(n)) for _ in range(n))
    dp[0][0] = MAP[0][0]
    heap = [[MAP[0][0], 0, 0]]
    hq.heapify(heap)

    while heap:
        price, a, b = hq.heappop(heap)
        if a == n-1 and b == n-1:
            print('Problem ', i, ': ', price, sep="")
        for x, y in zip(dx, dy):
            ax, by = a+x, b+y
            if 0 <= ax < n and 0 <= by < n and price+MAP[ax][by] < dp[ax][by]:
                dp[ax][by] = price+MAP[ax][by]
                hq.heappush(heap, [dp[ax][by], ax, by])
#######################################12-28############################################3
import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def djikstra():
    point = [(MAP[0][0],0,0)]
    MAP[0][0] == -1
    while point:
        dist, a, b = hq.heappop(point)
        if a == n-1 and b == n-1:
            return dist
        for x,y in zip(dx,dy):
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<n and MAP[ax][by]>=0:
                hq.heappush(point,(dist+MAP[ax][by], ax, by))
                MAP[ax][by] = -1

    return -1

i = 0
while True:
    i+=1
    n = int(read())
    if n == 0: break
    MAP=list(list(map(int,read().split())) for _ in range(n))
    print('Problem ',i,': ',djikstra(),sep='')
