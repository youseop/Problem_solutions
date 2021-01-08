import sys
# sys.stdin = open("text.txt","rt")
read=sys.stdin.readline
sys.setrecursionlimit(10000)
n,m = map(int,read().split())
trap = list(1 for _ in range(n+1))
for _ in range(m):
    i = int(read())
    trap[i] = 0
x = int((2*n)**0.5+1)
dp = list(list(-1 for _ in range(x)) for _ in range(n+1))
dp[n] = [0 for _ in range(x)]

def dfs(index,jump):
    if dp[index][jump] >= 0:
        return dp[index][jump]

    dp[index][jump] = sys.maxsize
    for j in [jump,jump-1,jump+1]:
        if j>0 and index + j<=n and trap[index+j]:
            dp[index][jump] = min(dp[index][jump],dfs(index+j,j)+1)
    return dp[index][jump]
dfs(1,0)
if dp[1][0] == sys.maxsize:
    print(-1)
else:
    print(dp[1][0])
# for d in dp:
#     print(d)