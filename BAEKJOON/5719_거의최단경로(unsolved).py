import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

def djikstra(start):
    cand = []
    def dfs(end, save):
        if end == start:
            cand.append(save)
            return
        for prev_node, dist in next[end]:
            if visit[prev_node] + dist == visit[end]: 
                dfs(prev_node, save+[prev_node])
        
    save = list(-1 for _ in range(n+1))
    point = [(0,start)]
    visit = list(inf for _ in range(n+1))
    visit[start] = 0
    while point:
        dist, node = hq.heappop(point)
        for next_node, weight in bridge[node]:
            if visit[next_node] > dist+weight:
                visit[next_node] = dist+weight
                save[next_node] = node
                hq.heappush(point,(visit[next_node], next_node))
    dfs(end,[end])
    return cand

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
            ##here
            if visit[next_node] > dist+weight:
                if node in check:
                    if next_node not in check[node]:
                        visit[next_node] = dist+weight
                        save[next_node] = node
                        hq.heappush(point,(visit[next_node], next_node))
                else:
                    visit[next_node] = dist+weight
                    save[next_node] = node
                    hq.heappush(point,(visit[next_node], next_node))

while True:
    n,m = map(int,read().split())
    if n == 0 and m == 0: break
    start, end = map(int,read().split())
    next = list([] for _ in range(n+1))
    bridge = list([] for _ in range(n+1))
    for _ in range(m):
        a,b,c = map(int,read().split())
        bridge[a].append((b,c))
        next[b].append((a,c))
    cand = djikstra(start)
    del next
    check = dict()
    for cand_ in cand:
        for i in range(len(cand_)-1):
            if cand_[i+1] not in check:
                check[cand_[i+1]] = set()
            check[cand_[i+1]].add(cand_[i])
    del cand
    answer = secondshort(start)
    if answer:
        print(answer)
    else:
        print(-1)