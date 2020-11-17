import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m,v=map(int,read().split())

bridge=dict()

for i in range(m):
    a,b=map(int,read().split())
    if a in bridge:
        bridge[a].append(b)
    else:
        bridge[a]=[b]
    if b in bridge:
        bridge[b].append(a)
    else:
        bridge[b]=[a]
for i in bridge:
    bridge[i].sort()

def DFS(v):
    flag=1
    print(v,end=' ')
    if check[v]==0:
        check[v]=1
    if v in bridge:
        for i in bridge[v]:
            if check[i]==0:
                DFS(i)
                flag=2
    if flag==1:
        return

check=[0 for _ in range(n+1)]
DFS(v)
print()

#BFS
from collections import deque

check=[0 for _ in range(n+1)]
check[v]=1
point=deque([v])

while point:
    flag=1
    for _ in range(len(point)):
        a=point.popleft()
        print(a,end=' ')
        if a in bridge:
            for i in bridge[a]:
                if check[i]==0:
                    point.append(i)
                    check[i]=1
                    flag=2
    if flag==1:
        break
