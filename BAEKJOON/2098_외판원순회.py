import sys
read=sys.stdin.readline
inf = sys.maxsize
n = int(read())
link = list(list(map(int,read().split())) for _ in range(n))
dp = list(list(inf for _ in range(2**(n-1))) for _ in range(n))
for i in range(n):
    dp[i][0] = 0
    if link[0][i]: 
        dp[i][1<<(i-1)] = link[0][i]

for i in range(1,2**(n-1)):
    for v in range(1,n):
        if 1<<(v-1) & i:
            for j in range(1,n):
                if 1<<(j-1)|i != i and link[v][j]!=0:
                        dp[j][1<<(j-1)|i] = min(\
                            dp[j][1<<(j-1)|i],\
                            dp[v][i]+link[v][j]\
                            )

print(min(list(dp[i][-1]+link[i][0] for i in range(n) if dp[i][-1]!=inf and link[i][0])))