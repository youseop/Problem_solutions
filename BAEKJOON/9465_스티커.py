import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    num = list(list(map(int, read().split())) for _ in range(2))
    dp = list([0, 0, 0] for _ in range(n))
    dp[0] = [num[0][0], num[1][0], 0]

    for i in range(1, n):
        dp[i] = [max(dp[i-1][1]+num[0][i], dp[i-1][2]+num[0][i]), max(dp[i-1]
                                                                      [0]+num[1][i], dp[i-1][2]+num[1][i]), max(dp[i-1][0], dp[i-1][1])]
    print(max(dp[-1]))
