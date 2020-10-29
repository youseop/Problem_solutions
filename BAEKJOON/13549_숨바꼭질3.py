from collections import deque
import sys
read = sys.stdin.readline
n, k = map(int, read().split())

len = 100_000

point = deque([n])
dp = list(-1 for _ in range(len*2+1))
dp[n] = 0

while point:
    a = point.popleft()
    if a == k:
        print(dp[a])
        break
    else:
        tmp = a
        while tmp < len*2 and tmp >= 1:
            if dp[tmp] == -1:
                point.append(tmp)
                dp[tmp] = dp[a]
            tmp = tmp*2

        if a-1 >= 0 and dp[a-1] == -1:
            dp[a-1] = dp[a]+1
            point.append(a-1)
        if a+1 <= len*2 and dp[a+1] == -1:
            dp[a+1] = dp[a]+1
            point.append(a+1)
