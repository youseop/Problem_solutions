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
