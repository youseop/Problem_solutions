import sys
read=sys.stdin.readline

n=int(read())
card=[0]+list(map(int,read().split()))

dp=list(2147000000 for _ in range(n+1))
dp[0]=0

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        for k in range(1,1+j//i):
            dp[j]=min(dp[j],dp[j-i*k]+card[i]*k)
print(dp[-1])