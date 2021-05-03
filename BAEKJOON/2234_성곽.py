import sys
from collections import deque
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

isInt = type(0)

def checkArea(MAP, check, index, *start):
    point = deque([start])
    cnt = 1
    check[start[0]][start[1]] = index
    while point:
        a,b = point.popleft()
        for i,x,y in [(1,0,-1),(2,-1,0),(4,0,1),(8,1,0)]:
            ax,by = a+x,b+y
            if 0<=ax<n and \
                0<=by<m and \
                check[ax][by] < 0 and \
                MAP[a][b]&i == 0:
                check[ax][by] = index
                point.append([ax,by])
                cnt += 1
    return cnt


def getArea(MAP, check, startingPoint):
    index = 0
    area = []
    for i in range(n):
        for j in range(m):
            if check[i][j] < 0:
                area.append(checkArea(MAP, check, index, i, j))
                startingPoint.append((i,j))
                index += 1
    return area


def checkAdjacent(MAP, check, i, j):
    point = deque([[MAP[i][j],i,j]])
    cnt = 0
    adjacentSet = set()
    index = check[i][j]
    
    while point:
        direction,a,b = point.popleft()
        cnt += 1
        for i,x,y in [(1,0,-1),(2,-1,0),(4,0,1),(8,1,0)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<m:
                if direction&i and check[ax][by] != index:
                    adjacentSet.add(check[ax][by])
                elif MAP[ax][by] >= 0:
                    point.append([MAP[ax][by],ax,by])
                    MAP[ax][by] = -1 
    return adjacentSet


def getAdjacent(MAP, check, startingPoint):
    adjacent=[]
    for a,b in startingPoint:
        adjacent.append(checkAdjacent(MAP, check, a, b))
    
    return adjacent


def getMaxAdjacent(adjacent, area):
    point = deque([0])
    maxAdjacent = 0
    visit = list(list(1 for _ in range(len(area))) for _ in range(len(area)))
    while point:
        a = point.popleft()
        for x in adjacent[a]:
            if visit[a][x]:
                visit[a][x] = 0
                visit[x][a] = 0
                maxAdjacent = max(maxAdjacent, area[a]+area[x])
                point.append(x)
    return maxAdjacent

m,n = map(int,read().split())
MAP = list(list(map(int,read().split())) for _ in range(n))
check = list(list(-1 for _ in range(m)) for _ in range(n))
startingPoint = []

area = getArea(MAP, check, startingPoint);

print(len(area)) #1
print(max(area)) #2

adjacent = getAdjacent(MAP, check, startingPoint);

print(getMaxAdjacent(adjacent, area)) #3


