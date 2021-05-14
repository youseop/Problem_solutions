class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(a,b):
            nonlocal dp, obstacleGrid, n, m
            if dp[a][b] != -1:
                return dp[a][b]
            cnt = 0
            for x,y in ((0,1),(1,0)):
                ax,by = a+x,b+y
                if 0<=ax<n and 0<=by<m and obstacleGrid[ax][by] == 0:
                    cnt += dfs(ax,by)
            dp[a][b] = cnt
            return cnt
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        dp = list(list(-1 for _ in range(m)) for _ in range(n))
        dp[-1][-1] = 1
        dfs(0,0)

        return dp[0][0]