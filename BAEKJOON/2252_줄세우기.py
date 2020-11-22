import heapq
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
check = list(0 for _ in range(n+1))
bridge = dict()
for _ in range(m):
    a, b = map(int, read().split())
    check[b] += 1
    if a in bridge:
        bridge[a].append(b)
    else:
        bridge[a] = [b]

point = []
for i in range(1, n+1):
    if check[i] == 0:
        point.append(i)

heapq.heapify(point)
while point:
    a = heapq.heappop(point)
    print(a, end=' ')
    if a in bridge:
        for x in bridge[a]:
            check[x] -= 1
            if check[x] == 0:
                heapq.heappush(point, x)
