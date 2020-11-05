import heapq
import sys
read = sys.stdin.readline
n, m = map(int, read().split())

bridge = list(dict() for _ in range(n+1))
for _ in range(m):
    a, b, c = map(int, read().split())
    if b in bridge[a]:
        bridge[a][b] = max(bridge[a][b], c)
    else:
        bridge[a][b] = c
    if a in bridge[b]:
        bridge[b][a] = max(bridge[b][a], c)
    else:
        bridge[b][a] = c

fac1, fac2 = map(int, read().split())

dp = list(0 for _ in range(n+1))
dp[fac1] = 2147000000
dp[0] = -1

save = []
heapq.heappush(save, [-2147000000, fac1])

while save:
    w, p = heapq.heappop(save)
    if p == fac2:
        break
    w = -w
    for p_new in bridge[p]:
        w_new = bridge[p][p_new]
        if dp[p_new] < min(dp[p], w_new):
            dp[p_new] = min(dp[p], w_new)
            heapq.heappush(save, [-dp[p_new], p_new])
print(dp[fac2])
