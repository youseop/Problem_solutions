import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)
inf = sys.maxsize
n = int(read())
mat = list(list(map(int,read().split())) for _ in range(n))
dp = list(list(inf for _ in range(n)) for _ in range(n))
for start in range(n):
    dp[start][start] = 0
    if start != n-1:
        end = start + 1
        dp[start][end] = mat[start][0]*mat[start][1]*mat[end][1]


def func(start,end):
    if start == end: return 0
    if dp[start][end]!=inf:
        return dp[start][end]
    
    for k in range(start, end):
        dp[start][end] = min(dp[start][end],func(start,k) + func(k+1,end) + mat[start][0]*mat[k][1]*mat[end][1])
    return dp[start][end]

func(0,n-1)
print(dp[0][-1])
#for d in dp:
#    print(d)
