import sys
import heapq as hq
read=sys.stdin.readline

n, e = map(int,read().split())
v = int(read())
bridge = [{} for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,read().split())
    if b not in bridge[a]:
        bridge[a][b] = c
    else:
        bridge[a][b] = min(c, bridge[a][b])


inf = sys.maxsize
visit = list(inf for _ in range(n+1))
visit[v] = 0

point = [(0 ,v)]
while point:
    dist, node = hq.heappop(point)
    for next_node in bridge[node].keys():
        if visit[next_node] > dist + bridge[node][next_node]:
            visit[next_node] = dist + bridge[node][next_node]
            hq.heappush(point, (visit[next_node], next_node))

for i in visit[1:]:
    if i != inf: print(i)
    else: print('INF')