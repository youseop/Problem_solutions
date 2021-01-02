import sys
read=sys.stdin.readline

n,m = map(int,read().split())
maise = list(list(map(int,read().split())) for _ in range(n))
dp = list(maise[i][:] for i in range(n))

for i in range(n):
    for j in range(m):
        for x,y in [(-1,0),(0,-1),(-1,-1)]:
            ix,jy = i+x,j+y
            if 0<=ix<n and 0<=jy<m:
                dp[i][j] = max(dp[i][j], dp[ix][jy]+maise[i][j])

print(dp[-1][-1])