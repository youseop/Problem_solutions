from collections import deque
import sys
read = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, read().split())

bridge = list([] for _ in range(n+1))
for _ in range(m):
    a, b, c = map(int, read().split())
    bridge[a].append([b, c])

dp = list(inf for _ in range(n+1))
dp[1] = 0

for node in range(n):
    for i in range(1, n+1):
        for next, w in bridge[i]:
            if dp[i] != inf and dp[next] > w+dp[i]:
                dp[next] = w+dp[i]
                if node == n-1:
                    print(-1)
                    sys.exit()

for d in dp[2:]:
    print(d if d != inf else -1)
