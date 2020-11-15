import sys
read = sys.stdin.readline

n = int(read())
# n이 홀수일 경우 벽을 채울 수 있는 방법이 없다.
if n % 2 == 1:
    print(0)
    sys.exit()
# 첫 번째 값에는 벽을 채울 수 있는 경우의 수,
# 두 번째 값에는 dp 첫 번째 값들의 총 합을 저장한다.
dp = list([0, 0] for _ in range(n//2+1))
dp[1] = [3, 3]

for i in range(2, n//2+1):
    dp[i][0] = dp[i-1][0]*3+dp[i-2][1]*2+2
    dp[i][1] = dp[i][0]+dp[i-1][1]

print(dp[-1][0])
