import sys
read = sys.stdin.readline

n = int(input())
num = list(list(map(int, read().split())) for _ in range(n))

dp = num[0][:]

for i in range(1, n):
    R = min(dp[1], dp[2])+num[i][0]

    G = min(dp[0], dp[2])+num[i][1]

    B = min(dp[1], dp[0])+num[i][2]

    dp[0], dp[1], dp[2] = R, G, B
print(min(dp))
