import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

n,m = map(int,read().split())
bridge = list([] for _ in range(n+1))
for _ in range(m):
    a,b,c = map(int,read().split())
    bridge[a].append((b,c))
    bridge[b].append((a,c))
answer = [[] for _ in range(n+1)]
def djikstra():
    point = [(0, 1)]
    visit = list(inf for _ in range(n+1))
    visit[1] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, weight in bridge[node]:
            if visit[next_node] > dist + weight:
                visit[next_node] = dist + weight
                hq.heappush(point,(visit[next_node], next_node))

    point = [(0, 1)]
    visit_restore = list(inf for _ in range(n+1))
    visit_restore[1] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, weight in bridge[node]:
            if visit_restore[next_node] > dist + weight and visit_restore[next_node]>visit[next_node] :
                visit_restore[next_node] = dist + weight
                hq.heappush(point,(visit_restore[next_node], next_node))
                answer[next_node] = [node,next_node]
print(len(list(i for i in answer if i)))
for i in answer:
    if i: print(*i)