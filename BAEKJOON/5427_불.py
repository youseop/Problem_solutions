import sys, math
read=sys.stdin.readline

from collections import deque

dx=[1,0,0,-1]
dy=[0,1,-1,0]

#불과 상근이가 번갈아가며 BFS로 한 단계씩 이동한다.
def BFS(start,fire):
    start = deque([start])

    cnt = 1

    while start or fire:
        for _ in range(len(fire)):
            a,b = fire.popleft()
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<m and MAP[ax][by] != '#':
                    MAP[ax][by] = '#'
                    fire.append([ax,by])

        for _ in range(len(start)):
            a,b = start.popleft()
            if a == 0 or a == n-1 or b ==0 or b== m-1:
                return cnt
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<m and MAP[ax][by] == '.':
                    MAP[ax][by] = '@'
                    start.append([ax,by])
        cnt +=1
    return "IMPOSSIBLE"

for _ in range(int(read())):
    m,n=map(int,read().split())
    MAP=list(list(i for i in read().strip()) for _ in range(n))
    fire = deque()
    start = ()
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == '*':
                fire.append([i,j])
            elif MAP[i][j] == '@':
                start = [i,j]
    
    print(BFS(start,fire))
