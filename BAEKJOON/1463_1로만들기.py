n = int(input())
dp = [-1 for _ in range(n+1)]
dp[1] = 0
for i in range(1, n+1):
    if dp[i] == -1:
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            if dp[i] > dp[i//3]+1:
                dp[i] = dp[i//3]+1
        if i % 2 == 0:
            if dp[i] > dp[i//2]+1:
                dp[i] = dp[i//2]+1

print(dp[n])
