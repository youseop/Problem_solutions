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
