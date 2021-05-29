import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque


def bfs(i,j,check,lev):
    point = deque([(i,j)])
    check[i][j] = 0
    while point:
        a,b = point.popleft()
        for x,y in ((1,0),(0,1),(-1,0),(0,-1)):
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<n and check[ax][by] and area[ax][by] > lev:
                point.append((ax,by))
                check[ax][by] = 0


def getSafeArea(lev):
    check = list(list(1 for _ in range(n)) for _ in range(n))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] and area[i][j] > lev:
                cnt += 1
                bfs(i,j,check,lev)

    return cnt 


if __name__ == '__main__':
    n = int(read())
    area = list(list(map(int,read().split())) for _ in range(n))
    min_lev,max_lev = sys.maxsize,0
    for a in area:
        min_lev = min(min_lev, min(a))
        max_lev = max(max_lev, max(a))

    maxSafeArea = 0
    for lev in range(min_lev-1,max_lev):
        maxSafeArea = max(maxSafeArea, getSafeArea(lev))

    print(maxSafeArea)