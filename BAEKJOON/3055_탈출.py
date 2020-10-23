import sys
read=sys.stdin.readline
from collections import deque

r,c=map(int,read().split())
#r - 세로, c - 가로
map=list(list(read().strip()) for _ in range(r))
#비버 - D, 고슴도치 - S

dx=[1,0,-1,0]
dy=[0,1,0,-1]

water_s=deque([])
water_tmp=deque([])
kak_s=deque([])
kak_tmp=deque([])
D=[0,0]

for i in range(r):
    for j in range(c):
        if map[i][j]=='*':
            water_s.append([i,j])
        elif map[i][j]=='S':
            kak_s.append([i,j])
            map[i][j]=0
        elif map[i][j]=='D':
            D=[i,j]


def kak():
    while kak_s:
        a,b=kak_s.popleft()
        #print(a,b,map[a][b])
        for x,y in zip(dx,dy):
            ax=a+x
            by=b+y
            if 0<=ax<r and 0<=by<c and map[ax][by]==".":
                if map[a][b]=='*':
                    continue
                kak_tmp.append([ax,by])
                map[ax][by]=map[a][b]+1
            elif ax==D[0] and by==D[1]: 
                if map[a][b]=='*':
                    print('KAKTUS')
                else: print(map[a][b]+1)
                sys.exit()
    for i in range(len(kak_tmp)):
        kak_s.append(kak_tmp.pop())


def water():
    while water_s:
        a,b=water_s.popleft()
        for x,y in zip(dx,dy):
            ax=a+x
            by=b+y
            if 0<=ax<r and 0<=by<c and (map[ax][by]!="X" and map[ax][by]!="D" and map[ax][by]!="*"):
                water_tmp.append([ax,by])
                map[ax][by]='*'
    for i in range(len(water_tmp)):
        water_s.append(water_tmp.pop())

while kak_s or water_s:
    kak()
    water()

print('KAKTUS')

