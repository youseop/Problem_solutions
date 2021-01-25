def solution(n, edge):
    answer = 0
    import sys
    from heapq import heapify, heappush, heappop
    bridge = dict()
    for a,b in edge:
        a,b = a-1,b-1
        if a not in bridge:
            bridge[a] = []
        if b not in bridge:
            bridge[b] = []
        bridge[a].append(b)
        bridge[b].append(a)
    
    point = [0]
    dist = list(sys.maxsize for _ in range(n))
    dist[0] = 0
    while point:
        a = heappop(point)
        for next_node in bridge[a]:
            if dist[next_node] > dist[a] + 1:
                dist[next_node] = dist[a] + 1
                heappush(point, next_node)
        
    max_d = max(dist)
    for d in dist:
        if d == max_d:
            answer += 1
    return answer