import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque


m,n,h = map(int,read().split())
MAP = list(list(list(map(int,read().split())) for _ in range(n)) for _ in range(h))

point = deque()
total_cnt = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if MAP[k][i][j] == 0:
                total_cnt += 1
            elif MAP[k][i][j] == 1:
                point.append((k,i,j))


cnt = 0
time = -1
while point:
    time+=1
    for _ in range(len(point)):
        a,b,c = point.popleft()
        for z,x,y in ((0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)):
            az,bx,cy = a+z,b+x,c+y
            if 0<=az<h and 0<=bx<n and 0<=cy<m and MAP[az][bx][cy]==0:
                MAP[az][bx][cy] = 1
                cnt += 1
                point.append((az,bx,cy))


if total_cnt == cnt:
    print(time)
else:
    print(-1)


