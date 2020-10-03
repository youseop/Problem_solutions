n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [dict() for _ in range(n+1)]

dp[1][1] = stair[0]
dp[1][2] = 0
if n > 1:
    dp[2][1] = stair[0]+stair[1]
    dp[2][2] = stair[1]

for i in range(1, n+1):

    if len(dp[i]) == 0:
        dp[i][1] = dp[i-1][2]+stair[i-1]
        dp[i][2] = max([dp[i-2][1]+stair[i-1], dp[i-2][2]+stair[i-1]])

print(max([dp[i][1], dp[i][2]]))


'''
import sys
sys.stdin = open('input.txt','rt')

n=int(input())
stair = list(int(sys.stdin.readline().strip()) for _ in range(n))
stair.insert(0,-1)

dp=list(0 for _ in range(n+1))
dp[1]=stair[1]
if n >1: dp[2]=stair[1]+stair[2]
for i in range(3,n+1):
    dp[i]=max(dp[i-2]+stair[i], dp[i-3]+stair[i]+stair[i-1] )

print(dp[n])
'''
