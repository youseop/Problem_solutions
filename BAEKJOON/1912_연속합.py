import sys
read = sys.stdin.readline

n = int(input())
num = list(map(int, read().split()))

dp = list(0 for _ in range(n))
dp[0] = num[0]
for i in range(1, n):
    dp[i] = max(num[i], dp[i-1]+num[i])
print(max(dp))
