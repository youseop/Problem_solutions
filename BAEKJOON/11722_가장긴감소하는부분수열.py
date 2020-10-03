import sys

n = int(input())
numbs = list(map(int, sys.stdin.readline().split()))

dp = list(1 for _ in range(n))
for i in range(1, n):
    for j in range(i):
        if numbs[j] > numbs[i] and dp[j] >= dp[i]:
            dp[i] = dp[j]+1
print(max(dp))
