import sys
read=sys.stdin.readline
from collections import deque

dx=[1,0,0,-1]
dy=[0,1,-1,0]

n=int(input())
height=list(list(map(int,read().split())) for _ in range(n))

#지역 최대, 최소 높이 저장
max_h=0
min_h=sys.maxsize
for h in height:
    for x in h:
        max_h=max(max_h,x)
        min_h=min(min_h,x)

#h높이만큼 물이 찼을 때, 안전영역 갯수 탐색
def safe(h):
    global count
    #해당 지역을 방문했는지 확인
    visit = list(list(True for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            #물에 잠기지 않았고, 최초로 방문하는 점들에 대해 탐색
            if visit[i][j] and height[i][j]>=h:
                #영역이 한 곳 추가 되었음으로 'count += 1'
                count+=1
                #BFS수행하며 물에 잠기지 않은 인접영역을 모두 방문처리
                point = deque([[i,j]])
                visit[i][j]=False
                while point:
                    a,b=point.popleft()
                    for x,y in zip(dx,dy):
                        ax,by=a+x,b+y
                        if 0<=ax<n and 0<=by<n and visit[ax][by] and height[ax][by]>=h:
                            visit[ax][by]=False
                            point.append([ax,by])

answer=1
for i in range(min_h,max_h+1):
    count=0
    safe(i)
    answer=max(answer,count)

print(answer)