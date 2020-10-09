import sys
n = int(input())

numbs = list(int(sys.stdin.readline()) for _ in range(n))

dp = list(0 for _ in range(n+1))

for i in range(n):
    for j in range(i):
        if numbs[i] > numbs[j]:
            if dp[i] <= dp[j]:
                dp[i] = dp[j]+1

    if dp[i] == 0:
        dp[i] = 1

print(n-max(dp))
