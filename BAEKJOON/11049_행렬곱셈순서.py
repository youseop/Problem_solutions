import sys

n = int(sys.stdin.readline())
m = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))


dp = list(list(0 for _ in range(n)) for _ in range(n))
# dp[i][i+1]=m[i][0]*m[i][1]*m[i+1][1]

for i in range(1, n):
    for j in range(n-i):
        dp[j][j+i] = 2147000000
        for k in range(i):
            if dp[j][j+i] < dp[j][j+k]+dp[j+k+1][i+j]:
                continue
            tmp = dp[j][j+k]+dp[j+k+1][i+j]+m[j][0]*m[j+k][1]*m[i+j][1]
            if tmp < dp[j][j+i]:
                dp[j][j+i] = tmp
# for x in dp:
#     print(x)
print(dp[0][-1])
