import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

def djikstra(start):
    def find(min_far):
        for i in range(n):
            if visit[i]+visit_rev[i] == min_far:
                for next_node, dist in bridge[i]:
                    
                    if visit[i]+dist+visit_rev[next_node] == min_far:
                        cand[i][next_node]=0
        return
        
    point = [(0,start)]
    visit = list(inf for _ in range(n+1))
    visit[start] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, weight in bridge[node]:
            if visit[next_node] > dist+weight:
                visit[next_node] = dist+weight
                hq.heappush(point,(visit[next_node], next_node))
    
    visit_rev = list(inf for _ in range(n+1))
    point = [(0,end)]
    visit_rev[end] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, weight in bridge_rev[node]:
            if visit_rev[next_node] > dist+weight:
                visit_rev[next_node] = dist+weight
                hq.heappush(point,(visit_rev[next_node], next_node))
    min_far = visit[end]
    #print(visit)
    #print(visit_rev)
    find(min_far)
    return 

def secondshort(start):
    save = list(-1 for _ in range(n+1))
    point = [(0,start)]
    visit = list(inf for _ in range(n+1))
    visit[start] = 0
    while point:
        dist, node = hq.heappop(point)
        if node == end:
            return dist
        for next_node, weight in bridge[node]:
            if visit[next_node] > dist+weight and cand[node][next_node]:
                visit[next_node] = dist+weight
                save[next_node] = node
                hq.heappush(point,(visit[next_node], next_node))

while True:
    n,m = map(int,read().split())
    if n == 0 and m == 0: break
    start, end = map(int,read().split())
    bridge = list([] for _ in range(n+1))
    bridge_rev = list([] for _ in range(n+1))
    for _ in range(m):
        a,b,c = map(int,read().split())
        bridge[a].append((b,c))
        bridge_rev[b].append((a,c))
    cand = list(list(1 for _ in range(n)) for _ in range(n))
    djikstra(start)
    answer = secondshort(start)
    if answer:
        print(answer)
    else:
        print(-1)

