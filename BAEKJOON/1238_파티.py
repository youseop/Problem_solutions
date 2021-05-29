import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

n,m,x = map(int,read().split())
bridge = list([] for _ in range(n+1))
bridge_to = list([] for _ in range(n+1))
for _ in range(m):
    a,b,c = map(int,read().split())
    bridge[a].append((b,c))
    bridge_to[b].append((a,c))

def djikstra_goback():
    point = [(0, x)]
    visit = list(inf for _ in range(n+1))
    visit[x] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, d in bridge[node]:
            if visit[next_node] > d+dist:
                visit[next_node] = d+dist
                hq.heappush(point,(visit[next_node], next_node))
    return visit[1:]

def djikstra_goto():
    point = [(0, x)]
    visit = list(inf for _ in range(n+1))
    visit[x] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, d in bridge_to[node]:
            if visit[next_node] > d+dist:
                visit[next_node] = d+dist
                hq.heappush(point,(visit[next_node], next_node))
    return visit[1:]

print(max(i+j for i,j in zip(djikstra_goback(), djikstra_goto())))


