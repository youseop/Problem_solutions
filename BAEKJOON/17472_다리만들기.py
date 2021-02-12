import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline
from collections import deque

def check_island(a,b,num):
    MAP[a][b] = num
    point = deque([(a,b)])
    while point:
        a,b = point.popleft()
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<m and MAP[ax][by]==1:
                MAP[ax][by] = num
                point.append((ax,by))

def check_bridge(a,b):
    for x,y in [(1,0),(0,1),(0,-1),(-1,0)]:
        ax,by = a+x,b+y
        while 0<=ax<n and 0<=by<m :
            if MAP[ax][by] == MAP[a][b]:
                break
            if MAP[ax][by] and MAP[ax][by] != MAP[a][b]:
                dist = max(abs(ax-a),abs(by-b))-1
                if dist == 1:
                    dist = 0
                    break
                if not bridge[MAP[a][b]][MAP[ax][by]]:
                    bridge[MAP[a][b]][MAP[ax][by]] = dist
                else:
                    bridge[MAP[a][b]][MAP[ax][by]] = min(bridge[MAP[a][b]][MAP[ax][by]], dist)
                if not bridge[MAP[ax][by]][MAP[a][b]]:
                    bridge[MAP[ax][by]][MAP[a][b]] = dist
                else:
                    bridge[MAP[ax][by]][MAP[a][b]] = min(bridge[MAP[ax][by]][MAP[a][b]], dist)
                
                break
            ax += x
            by += y

def find(a):
    if a == network[a]:
        return a
    network[a] = find(network[a])
    return network[a]

def union(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return

    if level[root_a] >= level[root_b]:
        if level[root_a] == level[root_b]:
            level[root_a] += 1
        network[root_b] = root_a
    else:
        network[root_a] = root_b

#10
n,m = map(int,read().split())
MAP = list(list(map(int,read().split())) for _ in range(n))
num = 2
for i in range(n):
    for j in range(m):
        if  MAP[i][j] == 1:
            check_island(i,j,num)
            num += 1

bridge = list(list(0 for _ in range(num)) for _ in range(num))
for i in range(n):
    for j in range(m):
        if MAP[i][j]:
            check_bridge(i,j)

import heapq as hq
cand = []
network = list(i for i in range(num))
level = list(0 for _ in range(num))

for i in range(num):
    for j in range(num):
        if bridge[i][j]:
            hq.heappush(cand,(bridge[i][j],i,j))

answer = 0
connect_cnt = 0
while cand:
    dist,a,b = hq.heappop(cand)
    if find(a)!=find(b):
        answer += dist
        connect_cnt += 1
        union(a,b)

if connect_cnt == num-3:
    print(answer)
else:
    print(-1)