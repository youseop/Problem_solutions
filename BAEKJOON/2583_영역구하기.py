import sys
read=sys.stdin.readline
sys.setrecursionlimit(10000)
n,m,k = map(int,read().split())
MAP = list(list(0 for _ in range(m)) for _ in range(n))
for _ in range(k):
    x,y,a,b = map(int,read().split())
    x, y, a, b = n-1-y, x, n-b, a-1
    for i in range(a,x+1):
        for j in range(y,b+1):
            MAP[i][j] = 1

def dfs(a,b):
    MAP[a][b] = 1
    cnt = 1
    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
        ax,by = a+x,b+y
        if 0<=ax<n and 0<=by<m and MAP[ax][by] == 0:
            cnt += dfs(ax,by)
    return cnt

answer = []
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            area = dfs(i,j)
            if area: answer.append(area) 
answer.sort()
print(len(answer))
print(*answer)
