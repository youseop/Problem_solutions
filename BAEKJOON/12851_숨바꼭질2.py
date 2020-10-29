from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
point = deque([n])
dp = list(-1 for _ in range(max(n, k)*2+1))
dp[n] = 0

cnt, time = 0, 0

while point:
    for _ in range(len(point)):
        a = point.popleft()
        if a == k:
            time = dp[a]
            cnt += 1
        else:
            if a-1 >= 0 and (dp[a-1] == -1 or dp[a]+1 == dp[a-1]):
                dp[a-1] = dp[a]+1
                point.append(a-1)
            if a+1 <= k*2 and (dp[a+1] == -1 or dp[a]+1 == dp[a+1]):
                dp[a+1] = dp[a]+1
                point.append(a+1)
            if a*2 <= k*2 and (dp[a*2] == -1 or dp[a]+1 == dp[a*2]):
                dp[a*2] = dp[a]+1
                point.append(a*2)
    if cnt != 0:
        break

print(time, cnt, sep='\n')
