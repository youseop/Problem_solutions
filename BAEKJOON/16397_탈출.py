from collections import deque
import sys
read = sys.stdin.readline

n, t, g = map(int, read().split())

dp = list(-1 for _ in range(100_000))
dp[n] = 0

point = deque([n])

flag = -1
while point:
    a = point.popleft()
    if a == g:
        flag = dp[a]
        break
    if a == 0 and dp[1] > dp[0]+1:
        dp[1] = dp[0]+1
        point.append(1)
    else:
        if a*2 < 100_000:
            tmp = str(a*2)
            if tmp[0] == '1':
                tmp = tmp[1:]
            else:
                tmp = str(int(tmp[0])-1)+tmp[1:]
            tmp = int(tmp)
            if dp[tmp] == -1 and tmp >= 0:
                dp[tmp] = dp[a]+1
                point.append(tmp)
        if a+1 < 100_000:
            if dp[a+1] == -1:
                dp[a+1] = dp[a]+1
                point.append(a+1)

if flag == -1 or flag > t:
    print("ANG")
else:
    print(flag)
