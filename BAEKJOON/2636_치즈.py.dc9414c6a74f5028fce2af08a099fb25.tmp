import sys
read=sys.stdin.readline
from collections import deque

h,w=map(int,read().split())
ch=list(list(map(int,read().split())) for _ in range(h))

dx=[1,0,0,-1]
dy=[0,1,-1,0]

point=deque([[0,0]])
outsideair=[]
while point:
    a,b=point.popleft()
    for x,y in zip(dx,dy):
        ax,by=a+x,b+y
        if 0<=ax<h and 0<=by<w and ch[ax][by]==0:
            point.append([ax,by])
            ch[ax][by]='*'
            outsideair.append([ax,by])

time=0
disappear_tmp=0
disappear=0
while True:
    disappear_tmp=disappear
    disappear=0
    outsideair_tmp=[]
    for a,b in outsideair:
        for x,y in zip(dx,dy):
            ax,by=a+x,b+y
            if 0<=ax<h and 0<=by<w and ch[ax][by]==1 and [ax,by] not in outsideair_tmp:
                outsideair_tmp.append([ax,by])
                disappear+=1
    tmp=[]
    for a,b in outsideair_tmp:
        ch[a][b]='*'
        point=deque([[a,b]])
        while point:
            a,b=point.popleft()
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<h and 0<=by<w and ch[ax][by]==0:
                    point.append([ax,by])
                    ch[ax][by]='*'
                    tmp.append([ax,by])

    outsideair_tmp+=tmp    
    outsideair=outsideair_tmp[::]
    if outsideair==[]:
        print(time)
        print(disappear_tmp)
        break

    time+=1