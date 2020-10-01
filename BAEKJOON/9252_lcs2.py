import sys
import heapq
a = input()
b = input()
a = '0'+a
b = '0'+b
dp = list(['']*(len(a)) for _ in range(len(b)))

for i in range(1, len(b)):
    tmp = ''
    for j in range(1, len(a)):
        dp[i][j] = dp[i-1][j]
        if b[i] == a[j]:
            tmp = dp[i-1][j-1]+b[i]
        if len(tmp) <= j+1 and len(dp[i][j]) < len(tmp):
            dp[i][j] = tmp

lcs = dp[-1][-1]
print(len(lcs))
if len(lcs) != 0:
    print(lcs)
