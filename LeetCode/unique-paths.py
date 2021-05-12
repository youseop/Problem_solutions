class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = max(1,m+n-2)
        n = max(1,n-1)
        m = max(1,m-1)
        tmp,a,b = 1,1,1
        for i in range(2,x+1):
            tmp *= i
            if i == n:
                a = tmp
            if i == m:
                b = tmp
        return tmp//(a*b)