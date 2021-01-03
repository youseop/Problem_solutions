import sys
read = sys.stdin.readline

n, k = map(int, read().split())

mul = 1
dp = dict()
dp[n] = 1
dp[k-1] = 1
dp[n+k-1] = 1
for i in range(1, n+k):
    mul *= i
    if i == n:
        dp[n] = mul
    elif i == k-1:
        dp[k-1] = mul
    elif i == n+k-1:
        dp[n+k-1] = mul

answer = (dp[n+k-1]//(dp[n]*dp[k-1])) % 1_000_000_000
print(answer)

#############################
import sys
read=sys.stdin.readline

n,m = map(int,read().split())

dp = list(list(1 for _ in range(m)) for _ in range(n+1))
for i in range(1,n+1):
    for j in range(1,m):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1_000_000_000
print(dp[-1][-1])