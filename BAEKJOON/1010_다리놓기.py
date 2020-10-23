import sys
read=sys.stdin.readline

N=int(read())
f=[]
t=[]
for _ in range(N):
    a,b=map(int,read().split())
    f.append(a)
    t.append(b)

n=max(f)
m=max(t)

dp=list(list(0 for _ in range(m)) for _ in range(n))

for i in range(n):
    dp[i][i]=1
for i in range(m):
    dp[0][i]=i+1
for i in range(1,n):
    for j in range(i+1,m):
        dp[i][j]=dp[i][j-1]+dp[i-1][j-1]

for a,b in zip(f,t):
    print(dp[a-1][b-1])