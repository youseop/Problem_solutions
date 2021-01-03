import sys
read=sys.stdin.readline

n,m = map(int,read().split())
dp = list(list(map(int,list(read().strip()))) for _ in range(n))
answer = dp[0][0]
for i in range(1,n):
    for j in range(1,m):
        min_size = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        if dp[i][j] and min_size<=dp[i][j-1] and min_size<= dp[i-1][j]  and min_size<=dp[i-1][j-1]:
            dp[i][j] = min_size+1
            answer = max(answer, min_size+1)

print(answer**2)