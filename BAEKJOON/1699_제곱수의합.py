import sys
read = sys.stdin.readline
inf=sys.maxsize
n=int(read())

dp=list(inf for _ in range(n+1))
dp[1]=1

for i in range(1,n+1):
    if int(i**0.5)**2==i:
        dp[i]=1
    else:
        for j in range(1,i//2+1):
            dp[i]=min(dp[i],dp[j]+dp[i-j])
print(dp[-1])
