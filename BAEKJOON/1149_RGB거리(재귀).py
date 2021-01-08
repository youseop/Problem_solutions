import sys
read=sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(read())
rgb = list(list(map(int,read().split())) for _ in range(n))
dp = list([-1,-1,-1] for _ in range(n))
dp[-1]=rgb[-1][:]
def dfs(index, x):
    if dp[index][x] != -1:
        return dp[index][x]
    dp[index][x] = sys.maxsize
    for i in range(3):
        if i != x:
            dp[index][x] = min(dp[index][x], dfs(index+1,i)+rgb[index][x])

    return dp[index][x]

dfs(0,0)
dfs(0,1)
dfs(0,2)

print(min(dp[0]))