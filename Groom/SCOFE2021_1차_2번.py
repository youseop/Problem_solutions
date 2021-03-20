# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
read = sys.stdin.readline

n = int(read())
available = [0]+list(map(int,read().strip()))

dp = list(0 for _ in range(n+1))
dp[1] = 1
for i in range(2,n+1):
	if available[i]:
		dp[i] = dp[i-1] + dp[i-2]
		
print(dp[-1])
	