class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = m+n-2
        dp = list(1 for _ in range(x+1))
        for i in range(2,x+1):
            dp[i] = dp[i-1]*i
        
        return dp[n+m-2]//(dp[n-1]*dp[m-1])