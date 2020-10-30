import sys
read = sys.stdin.readline

n = int(read())
dp = list(list(0 for _ in range(10)) for _ in range(n+1))

for i in range(10):
    dp[1][i] = 1
for i in range(n+1):
    dp[i][0] = 1

for i in range(2, n+1):
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 10_007

print(sum(dp[-1]) % 10_007)
