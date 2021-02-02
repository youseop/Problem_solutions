import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline
from collections import deque

def find(a):
    if union[a] == a:
        return a
    union[a] = find(union[a])
    return union[a]

def merge(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return

    if level[root_a] >= level[root_b]:
        if level[root_a] == level[root_b]:
            level[root_a] += 1
        union[root_b] = root_a
    else:
        union[root_a] = root_b
    return

def union_water(a,b):
    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
        ax,by = a+x,b+y
        if 0<=ax<n and 0<=by<m and MAP[ax][by]=='.':
            merge(ax*m+by,a*m+b)

def melt_ice(a,b):
    point = deque([(a,b)])
    visit[a][b] = 0
    while point:
        a,b = point.popleft()
        save_water_point = []
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<m and visit[ax][by]:
                if MAP[ax][by]=='.':
                    save_water_point.append((ax,by))
                else:
                    point.append((ax,by))
                    visit[ax][by] = 0
        if save_water_point:
            for water in save_water_point:
                MAP[a][b] = '.'
                union_water(*water)
        else:
            ice.append((a,b))

                

n,m = map(int,read().split())
MAP = list(list(read().strip()) for _ in range(n))
union = list(i for i in range(n*m+1))
level = list(1 for _ in range(n*m+1))
#find(a*m + b)

swan = []
ice = deque()
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 'L':
            swan.append((i,j))
            MAP[i][j] = '.'
            union_water(i,j)
        elif MAP[i][j] == '.':
            union_water(i,j)
        else:
            ice.append((i,j))

time = 0
while ice:
    #for mm in MAP:
    #    print(mm)
    if find(swan[0][0]*m+swan[0][1]) == find(swan[1][0]*m+swan[1][1]):
        break
    visit = list(list(1 for _ in range(m)) for _ in range(n))
    for _ in range(len(ice)):
        i,j = ice.popleft()
        if MAP[i][j] == 'X':
            melt_ice(i,j)
    time += 1

print(time)