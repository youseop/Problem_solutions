import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

from collections import deque
import heapq as hq

def dijkstra():
    point = [(1,0,0,0)] #dist,i,j,k(높이)
    check[0][0][0] = 0

    while point:
        dist,x,y,h = hq.heappop(point)
        if x==n-1 and y == m-1: return dist
        for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<m and check[ax][by][h]:
                if MAP[ax][by] and h == 0:
                    hq.heappush(point,(dist+1,ax,by,1))
                    check[ax][by][1] = 0
                elif MAP[ax][by]==0:
                    hq.heappush(point,(dist+1,ax,by,h))
                    check[ax][by][h] = 0
    return -1


n,m = map(int,read().split())
MAP = list(list(int(i) for i in read().strip()) for _ in range(n))
check = list(list(list(1 for _ in range(2)) for _ in range(m)) for _ in range(n))

print(dijkstra())