class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = list(list(0 for _ in range(n)) for _ in range(n))

        answer = s[0]

        for i in range(n):
            dp[i][i] = s[i]
            if i != 0 and s[i]==s[i-1]:
                dp[i-1][i] = s[i-1:i+1]
                answer = dp[i-1][i]

        for k in range(2,n):
            for i in range(n-k):
                if s[i] == s[i+k] and dp[i+1][i+k-1]:
                    dp[i][i+k] = s[i]+dp[i+1][i+k-1]+s[i]
                    answer = dp[i][i+k]    
        return answer