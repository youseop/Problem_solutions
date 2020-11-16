def solution(n):
    answer = 0
    dp = list(1 for _ in range(2*n+1))
    for i in range(2, 2*n+1):
        dp[i] = dp[i-1]*i

    answer = dp[2*n]//(dp[n]*dp[n]*(n+1))

    return answer
