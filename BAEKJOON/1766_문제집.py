import heapq as hq
from collections import deque
import sys
read = sys.stdin.readline

point = []
hq.heapify(point)

n, m = map(int, read().split())
need = dict()
dp = list(0 for _ in range(n+1))

for _ in range(m):
    a, b = map(int, read().split())
    dp[b] += 1
    if a in need:
        need[a].append(b)
    else:
        need[a] = [b]
for i in range(1, n+1):
    if dp[i] == 0:
        hq.heappush(point, i)

while point:
    a = hq.heappop(point)
    print(a, end=' ')
    if a in need:
        for i in need[a]:
            dp[i] -= 1
            if dp[i] == 0:
                hq.heappush(point, i)
