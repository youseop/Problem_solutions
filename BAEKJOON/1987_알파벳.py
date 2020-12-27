import sys
from collections import deque
read=sys.stdin.readline

n,m = map(int,read().split())
board = list(list(read().strip()) for _ in range(n))

def BFS():
    cnt = 0
    point = set()
    point.add((0,0,board[0][0]))
    while point:
        a,b, way = point.pop()
        cnt = max(cnt, len(way))
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<m and board[ax][by] not in way:
                point.add((ax,by,way+board[ax][by]))
    return cnt

print(BFS())