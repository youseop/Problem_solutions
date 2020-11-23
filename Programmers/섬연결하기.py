def solution(n, costs):
    answer = 2147000000
    # 연결 정보를 dictionary에 저장
    bridge = dict()
    for a, b, c in costs:
        if a in bridge:
            bridge[a].append((b, c))
        else:
            bridge[a] = [(b, c)]
        if b in bridge:
            bridge[b].append((a, c))
        else:
            bridge[b] = [(a, c)]

    import heapq as hq

    def short(x):
        shortest = 0
        # 섬 방문여부
        check = list(True for _ in range(n))
        point = [[0, x]]
        # 길이가 가장 짧은 간선부터 탐색해 나가기 위해서 heapq사용
        hq.heapify(point)

        while point:
            dist, a = hq.heappop(point)
            # 해당 점을 아직 탐색하지 않은 경우에만 탐색한다.
            if check[a] == True:
                check[a] = False
                shortest += dist
                if a in bridge:
                    for i, w in bridge[a]:
                        if check[i]:
                            hq.heappush(point, [w, i])
        return shortest
    # 모든 점이 최단거리로 연결되어야 하기 때문에 어떤 점에서 시작하더라도 같은 값이 나온다.
    answer = short(0)

    return answer
