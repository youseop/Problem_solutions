from collections import deque
import sys
read = sys.stdin.readline
inf = sys.maxsize
n, m = map(int, read().split())
bridge = dict()
for _ in range(m):
    a, b, c = map(int, read().split())
    if a in bridge:
        bridge[a].append([b, c])
    else:
        bridge[a] = [[b, c]]
dp = list(inf for _ in range(n+1))
dp[1] = 0
check = list(0 for _ in range(n+1))

point = deque([1])
check[1] = 1

while point:
    a = point.popleft()
    check[a] *= (-1)
    if a in bridge:
        for i, w in bridge[a]:
            if dp[i] > dp[a]+w:
                dp[i] = dp[a]+w
                if check[i] <= 0:
                    check[i] = check[i]*(-1)+1
                    point.append(i)
                    if check[i] >= n:
                        print(-1)
                        sys.exit()
for i in dp[2:]:
    if i == inf:
        print(-1)
    else:
        print(i)
