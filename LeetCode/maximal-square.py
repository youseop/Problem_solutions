class Solution:
    def maximalSquare(self, dp: List[List[str]]) -> int:
        n,m = len(dp),len(dp[0])
        res = 0
        for i in range(n):
            if dp[i][0]=='1':
                res = 1
                break
        for j in range(m):
            if dp[0][j]=='1':
                res = 1
                break
            
        for i in range(1,n):
            for j in range(1,m):
                if dp[i][j] =='1':
                    dp[i][j] = 1+min(int(dp[i-x][j-y]) for x,y in ((1,1),(0,1),(1,0)))
                    res = max(res,int(dp[i][j]))
                    
        return res**2