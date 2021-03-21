import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

n = int(read())
dp = list(0 for _ in range(n))
for i in range(n):
    tmp = list(map(int,read().split()))
    tmp[0] += dp[0]
    for j in range(1,i):
        tmp[j] += max(dp[j],dp[j-1])
    tmp[i] += dp[i-1]
    dp = tmp
print(max(dp))