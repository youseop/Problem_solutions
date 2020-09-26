n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [dict() for _ in range(n+1)]

dp[1][1] = stair[0]
dp[1][2] = 0
if n > 1:
    dp[2][1] = stair[0]+stair[1]
    dp[2][2] = stair[1]

for i in range(1, n+1):

    if len(dp[i]) == 0:
        dp[i][1] = dp[i-1][2]+stair[i-1]
        dp[i][2] = max([dp[i-2][1]+stair[i-1], dp[i-2][2]+stair[i-1]])

print(max([dp[i][1], dp[i][2]]))
