# BFS와 DFS에 대해 더 공부해야겠다...
# Solved X
'''
import sys
sys.stdin = open("input.txt","rt")
read=sys.stdin.readline

n,m,fuel=map(int,read().split())
MAP=list(list(map(int,read().split())) for _ in range(n))
x,y=map(int,read().split())
tmp=list(list(map(int,read().split())) for _ in range(m))
FromTo=list(list([] for _ in range(n)) for _ in range(n))
for t in tmp:
    if FromTo[t[0]-1][t[1]-1]: FromTo[t[0]-1][t[1]-1].append([t[2]-1,t[3]-1])
    else: FromTo[t[0]-1][t[1]-1]=[[t[2]-1,t[3]-1]]


dx=[-1,0,1,0]
dy=[0,-1,0,1]

from collections import deque

def find_person():
    if len(bfs)==0:
        print(-1)
        sys.exit()
    a,b=bfs.popleft()
    if FromTo[a][b]:
        tmp=FromTo[a][b].pop()
        return [[a,b],tmp,check[a][b]]

    for da,db in zip(dx,dy):
        X=a+da
        Y=b+db
        if 0<=X<n and 0<=Y<n and MAP[X][Y]==0 and check[X][Y]==0:
            check[X][Y]=check[a][b]+1
            bfs.append([X,Y])
    
    return find_person()



def find_distance(tox,toy):
    if len(bfs_d)==0:
        print(-1)
        sys.exit()
    a,b=bfs_d.popleft()
    if a == tox and b==toy:
        return check[a][b]
    for da,db in zip(dx,dy):
        X=a+da
        Y=b+db
        if 0<=X<n and 0<=Y<n and MAP[X][Y]==0 and check[X][Y]==0:
            check[X][Y]=check[a][b]+1
            bfs_d.append([X,Y])
    return find_distance(tox,toy)

bfs=deque([[x-1,y-1]])
for _ in range(m):
    check=list(list(0 for _ in range(n)) for _ in range(n))
    aa,bb,d_1=find_person()
    #print(aa,bb,d_1)

    check=list(list(0 for _ in range(n)) for _ in range(n))
    bfs_d=deque([[aa[0],aa[1]]])
    d_2=find_distance(bb[0],bb[1])
    bfs=deque([[bb[0],bb[1]]])
    if d_1+d_2>fuel:
        print(-1)
        sys.exit()
    else: fuel=fuel-d_1+d_2
print(fuel)
'''
# 두번째시도,,, 왜이렇게 풀릴듯 하면서 안풀리는지 모르겠다.
'''
import sys
read=sys.stdin.readline
from collections import deque

n,m,fuel=map(int,read().split())

MAP=list(list(map(int,read().split())) for _ in range(n))
a,b=list(map(int,read().split()))
start=[a-1,b-1]
pas=dict()
checkpas=dict()
for _ in range(m):
    a,b,c,d=map(int,read().split())
    pas[(a-1,b-1)]=(c-1,d-1)
    checkpas[(a-1,b-1)]=True

dx=[1,0,0,-1]
dy=[0,1,-1,0]

def findPAS(start):
    check=list(list(True for _ in range(n)) for _ in range(n))
    point=deque([start])
    far=0
    same_far=[]
    while point:
        term=len(point)
        for _ in range(term):
            a,b=point.popleft()
            check[a][b]=False
            if (a,b) in pas and checkpas[(a,b)]:
                same_far.append([far, (a,b)])
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    point.append([ax,by])
        far+=1
        if far>fuel:break
        if same_far:
            same_far.sort(key=lambda x : (x[1][0],x[1][1]))
            return same_far[0]

    print(-1)
    sys.exit()
    return

def takePAS(a,b):
    check=list(list(True for _ in range(n)) for _ in range(n))
    c,d=pas[(a,b)]
    point=deque([[a,b]])
    far=0
    while point:
        term=len(point)
        for _ in range(term):
            a,b=point.popleft()
            check[a][b]=False
            if c==a and d==b:
                return far
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    point.append([ax,by])
        far+=1
        if len_From+far>fuel: break
    print(-1)
    sys.exit()
    return

point=0

for _ in range(m):
    len_From,point=findPAS(start)
    len_To=takePAS(point[0],point[1])

    if fuel<len_From+len_To:
        print(-1)
        sys.exit()

    fuel=fuel-len_From+len_To

    start=pas[point[0],point[1]]
    checkpas[(point[0],point[1])]=False

print(fuel)
'''
