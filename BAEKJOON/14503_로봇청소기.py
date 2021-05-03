import sys
from collections import deque
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

direction = [(-1,0),(0,1),(1,0),(0,-1)]


def dfs(a,b,d):
    cnt = 0
    if MAP[a][b] == 0:
        cnt += 1
        MAP[a][b] = -1
    if all(MAP[a+x][b+y]!=0 for x,y in direction):
        a,b = a-direction[d][0],b-direction[d][1]
        if MAP[a][b] != 1:
            cnt += dfs(a,b,d)
        return cnt
    
    for _ in range(4):
        d = (d+3)%4
        ad,bd = a+direction[d][0],b+direction[d][1]
        if MAP[ad][bd] == 0:
            cnt += dfs(ad, bd, d)
            break
    return cnt


n,m = map(int,read().split())
r,c,d = map(int,read().split())
MAP = list(list(map(int,read().split())) for _ in range(n))

print(dfs(r,c,d))