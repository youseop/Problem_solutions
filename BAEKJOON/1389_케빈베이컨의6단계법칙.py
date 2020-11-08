from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())

friend = dict()
for _ in range(m):
    a, b = map(int, read().split())
    if a in friend:
        if b not in friend[a]:
            friend[a].append(b)
    else:
        friend[a] = [b]
    if b in friend:
        if a not in friend[b]:
            friend[b].append(a)
    else:
        friend[b] = [a]

res = []
for i in range(1, n+1):
    dp = list(2147000000 for _ in range(n+1))
    dp[i] = 0
    dp[0] = 0
    point = deque([i])
    while point:
        a = point.popleft()
        for x in friend[a]:
            if dp[x] > dp[a]+1:
                dp[x] = dp[a]+1
                point.append(x)
    res.append([sum(dp), i])
res.sort(key=lambda x: (x[0], x[1]))
print(res[0][1])
