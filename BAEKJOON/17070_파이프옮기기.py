import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(read())
MAP = list(list(map(int,read().split())) for _ in range(n))
dp = list(list(list(-1 for _ in range(3)) for _ in range(n)) for _ in range(n))
dp[-1][-1] = [1,1,1]

def dfs(a,b,d):
    if dp[a][b][d] != -1:
        return dp[a][b][d]
    dp[a][b][d] = 0
    
    if d == 2:
        for x,y,new_d in [(0,1,2),(1,1,1)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<n and MAP[ax][by] == 0:
                if new_d == 1:
                    if MAP[ax][by-1] == 0 and MAP[ax-1][by] == 0: 
                        dp[a][b][d] += dfs(ax,by,new_d)
                else:
                    dp[a][b][d] += dfs(ax,by,new_d)
    elif d == 1:
        for x,y,new_d in [(0,1,2),(1,1,1),(1,0,0)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<n and MAP[ax][by] == 0:
                if new_d == 1:
                    if MAP[ax][by-1] == 0 and MAP[ax-1][by] == 0: 
                        dp[a][b][d] += dfs(ax,by,new_d)
                else:
                    dp[a][b][d] += dfs(ax,by,new_d)
    else:
        for x,y,new_d in [(1,1,1),(1,0,0)]:
            ax,by = a+x,b+y
            if 0<=ax<n and 0<=by<n and MAP[ax][by] == 0:
                if new_d == 1:
                    if MAP[ax][by-1] == 0 and MAP[ax-1][by] == 0: 
                        dp[a][b][d] += dfs(ax,by,new_d)
                else:
                    dp[a][b][d] += dfs(ax,by,new_d)
    return dp[a][b][d]

print(dfs(0,1,2))