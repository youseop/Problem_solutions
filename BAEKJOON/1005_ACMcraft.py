from collections import deque
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, k = map(int, read().split())
    time = [0]+list(map(int, read().split()))
    bridge = dict()
    left = list(0 for _ in range(n+1))
    dp = list(0 for _ in range(n+1))

    for _ in range(k):
        a, b = map(int, read().split())
        left[b] += 1
        if a not in bridge:
            bridge[a] = []
        bridge[a].append(b)

    NEED = int(read())

    point = deque([])
    for i in range(1, n+1):
        if left[i] == 0:
            point.append(i)
            dp[i] = time[i]

    while point:
        a = point.popleft()
        if a == NEED:
            print(dp[a])
            break
        if a in bridge:
            for i in bridge[a]:
                left[i] -= 1
                dp[i] = max(dp[i], dp[a]+time[i])
                if left[i] == 0:
                    point.append(i)
