import sys
read = sys.stdin.readline

n = int(read())

num = list(map(int, read().split()))

dp = list([0, 0] for _ in range(n))
dp[0] = [num[0], num[0]]
answer = num[0]
for i in range(1, n):
    dp[i][0] = max(num[i], dp[i-1][0]+num[i])
    dp[i][1] = max(dp[i][0], dp[i-1][0], dp[i-1][1]+num[i])
    answer = max(answer, dp[i][1])
print(answer)
