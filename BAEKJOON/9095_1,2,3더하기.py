for _ in range(int(input())):
    n = int(input())
    dp = list(-1 for _ in range(n+1))
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    if n > 2:
        dp[3] = 4

    for i in range(1, n+1):
        if dp[i] != -1:
            continue
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[-1])
