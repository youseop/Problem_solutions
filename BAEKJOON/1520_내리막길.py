# 시행착오!!
'''
import sys
read=sys.stdin.readline

m,n=map(int,read().split())
stairs=list(list(map(int,read().split())) for _ in range(m))

dp=list(list(0 for _ in range(n)) for _ in range(m))

for i in range(n):
    dp[0][i]=1

for i in range(1,m):
    save=list(0 for _ in range(n))
    for j in range(n):
        if stairs[i][j]<stairs[i-1][j]: 
            save[j]=dp[i-1][j]
            dp[i][j]=dp[i-1][j]
    for j in range(n):
        x,y=j,j
        while True:
            if x<=0 or stairs[i][x]>=stairs[i][x-1]: break
            dp[i][j]+=save[x-1]
            x-=1
        while True:
            if y+1>=n or stairs[i][y]>=stairs[i][y+1]: break
            dp[i][j]+=save[y+1]
            y+=1
        #print('save:',save)

print(dp[-1][-1])'''
