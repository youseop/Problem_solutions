import sys
read=sys.stdin.readline

n=int(read())

dp=list([-1,-1] for _ in range(n+1))
dp[1]=[0,0]
for i in range(2,n+1):
    dp[i]=[dp[i-1][0]+1,i-1]
    if i%2==0:
        if dp[i][0]>dp[i//2][0]: dp[i]=[dp[i//2][0]+1,i//2]
    if i%3==0:
        if dp[i][0]>dp[i//3][0]: dp[i]=[dp[i//3][0]+1,i//3]
     
a,b=dp[-1][0],dp[-1][1]
print(dp[-1][0])
print(n,end=' ')
while a!=0:
    print(b,end=' ')
    a,b=dp[b][0],dp[b][1]