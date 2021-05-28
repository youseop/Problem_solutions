import sys
read = sys.stdin.readline
from heapq import heappush, heappop

DANGEROUS_AREA = 1
DEATH_AREA = -1


def printMAP():
    for mm in MAP:
        print(*mm)


def getAreaInfo(flag):
    for _ in range(int(read())):
        x1,y1,x2,y2 = map(int,read().split())
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                MAP[i][j] = flag


def bfs():
    point = [(0,0,0)]
    MAP[0][0] = -1
    while point:
        d,a,b = heappop(point)
        if a == 500 and b == 500:
            return d

        for x,y in ((1,0),(0,1),(-1,0),(0,-1)):
            ax,by = a+x,b+y
            if 0<=ax<=500 and 0<=by<=500:
                if MAP[ax][by] == 0:
                    heappush(point,(d,ax,by))
                elif MAP[ax][by] == 1:
                    heappush(point,(d+1,ax,by))
                MAP[ax][by] = -1

    return -1

if __name__ == '__main__':
  MAP = list(list(0 for _ in range(501)) for _ in range(501))
  getAreaInfo(DANGEROUS_AREA)
  getAreaInfo(DEATH_AREA)

  res = bfs()

  print(res)