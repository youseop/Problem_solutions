import sys
read = sys.stdin.readline

n = int(read())
dp = list(list(0 for _ in range(2)) for _ in range(n+1))

dp[1] = [0, 1]

for i in range(2, n+1):
    dp[i][1] = dp[i-1][0]
    dp[i][0] = sum(dp[i-1])

print(sum(dp[-1]))
