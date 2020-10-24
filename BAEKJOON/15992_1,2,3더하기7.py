
import sys
read = sys.stdin.readline

n = int(read())
answer = []
m = 0
for _ in range(n):
    a, b = map(int, read().split())
    answer.append([a, b])
    m = max(a, m)


dp = list(list(0 for _ in range(m+1)) for _ in range(m+1))
dp[1][1] = 1
if m > 1:
    dp[2][1] = 1
    dp[2][2] = 1
if m > 2:
    dp[3][1] = 1
    dp[3][2] = 2
    dp[3][3] = 1
# check=1
for i in range(4, m+1):
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1]) % 1_000_000_009
        #if dp[i][j]==0: check+=1

for a, b in answer:
    print(dp[a][b])
