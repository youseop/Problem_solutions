import sys
read=sys.stdin.readline

n = int(read())
dp = list(0 for _ in range(n+1))
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])