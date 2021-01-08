import sys
read=sys.stdin.readline
inf = sys.maxsize
def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

n = int(read())
link = list(list(0 for _ in range(n)) for _ in range(n))
city = list(list(map(int,read().split())) for _ in range(n))
for i in range(n):
    for j in range(n):
        link[i][j] = dist(city[i],city[j])

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