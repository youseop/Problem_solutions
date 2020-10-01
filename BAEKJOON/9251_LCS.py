import sys
import heapq
a = input()
b = input()
a = '0'+a
b = '0'+b
dp = list([0]*(len(a)) for _ in range(len(b)))

for i in range(1, len(b)):
    tmp = 0
    for j in range(1, len(a)):
        dp[i][j] = dp[i-1][j]
        if b[i] == a[j]:
            tmp = dp[i-1][j-1]+1
        if tmp <= j+1 and dp[i][j] < tmp:
            dp[i][j] = tmp
print(max(dp[-1]))


'''Test case

AGGTAB
GXTXAYB
'''
