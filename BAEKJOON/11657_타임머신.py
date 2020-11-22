from collections import deque
import sys
read = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, read().split())
bridge = list([] for _ in range(n+1))
for _ in range(m):
    a, b, c = map(int, read().split())
    bridge[a].append([b, c])
# 1번 노드로 부터의 거리 저장
dp = list(inf for _ in range(n+1))
dp[1] = 0
# deque내에 점이 포함되어 있는지 검사 + 방문 횟수 검사
# 양수면 deque내에 포함
check = list(0 for _ in range(n+1))

point = deque([1])
check[1] = 1

while point:
    a = point.popleft()
    check[a] *= (-1)
    for i, w in bridge[a]:
        if dp[i] > dp[a]+w:
            dp[i] = dp[a]+w
            if check[i] <= 0:
                check[i] = check[i]*(-1)+1
                point.append(i)
                if check[i] >= n:
                    print(-1)
                    sys.exit()
for d in dp[2:]:
    print(d if d != inf else -1)
