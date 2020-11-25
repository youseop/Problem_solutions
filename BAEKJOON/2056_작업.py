from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
bridge = dict()
time = list(0 for _ in range(n+1))
left = list(0 for _ in range(n+1))

for i in range(1, 1+n):
    tmp = list(map(int, read().split()))
    if tmp[1] != 0:
        for j in range(2, tmp[1]+2):
            if tmp[j] not in bridge:
                bridge[tmp[j]] = []
            bridge[tmp[j]].append(i)
    left[i] = tmp[1]
    time[i] = tmp[0]

dp = list(0 for _ in range(n+1))

point = deque([])
for i in range(1, n+1):
    if left[i] == 0:
        point.append(i)
        dp[i] = time[i]

while point:
    a = point.popleft()
    if a in bridge:
        for i in bridge[a]:
            left[i] -= 1
            dp[i] = max(dp[i], dp[a]+time[i])
            if left[i] == 0:
                point.append(i)
print(max(dp))
