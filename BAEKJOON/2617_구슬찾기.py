import sys
from collections import deque
read=sys.stdin.readline

def bfs_forw(index):
    global total_cnt
    cnt = 0
    point = deque([index])
    visit = list(1 for _ in range(n+1))
    visit[index] = 0
    while point:
        a = point.popleft()
        for i in forw[a]:
            if visit[i]:
                visit[i] = 0
                cnt += 1
                if cnt > n//2: 
                    total_cnt+=1
                    return
                point.append(i)
    return

def bfs_backw(index):
    global total_cnt
    cnt = 0
    point = deque([index])
    visit = list(1 for _ in range(n+1))
    visit[index] = 0
    while point:
        a = point.popleft()
        for i in backw[a]:
            if visit[i]:
                visit[i] = 0
                cnt += 1
                if cnt > n//2: 
                    total_cnt+=1
                    return
                point.append(i)
    return

n,m = map(int,read().split())
forw = list([] for _ in range(n+1))
backw = list([] for _ in range(n+1))
for _ in range(m):
    a,b = map(int,read().split())
    forw[a].append(b)
    backw[b].append(a)
total_cnt = 0
for i in range(1,n+1):
    bfs_forw(i)
    bfs_backw(i)

print(total_cnt)