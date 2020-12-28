import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

n,m=map(int,read().split())
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,read().split())
    bridge[a].append([b,c])
    bridge[b].append([a,c])
v1,v2 = map(int,read().split())

def min_dist(start):
    visit = list(inf for _ in range(n+1))
    visit[start] = 0
    point = [(0, start)]

    while point :
        dist, node = hq.heappop(point)
        for index, d in bridge[node]:
            if d:
                if d+dist < visit[index]:
                    visit[index] = d+dist
                    hq.heappush(point,(visit[index], index))
    return visit

a = min_dist(1)
b = min_dist(v1)
c = min_dist(v2)
minDist = min(a[v1]+b[v2]+c[n],a[v2]+b[n]+c[v1])
if minDist >= inf:
    print(-1)
else:
    print(minDist)

