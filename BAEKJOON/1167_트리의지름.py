import sys
import heapq
from collections import deque
read = sys.stdin.readline
inf = sys.maxsize

v = int(read())
bridge = dict()
for _ in range(v):
    tmp = list(map(int, read().split()))
    bridge[tmp[0]-1] = []
    i = 1
    while True:
        if tmp[i] == -1:
            break
        bridge[tmp[0]-1].append([tmp[i+1], tmp[i]-1])
        i += 2

# x Node로 부터 가장 먼 점의 거리 & 좌표 추출 - 다익스트라 알고리즘 활용


def bfs_far(x):
    # 가장 먼 점의 거리, 좌표 저장
    save = [0, 0]
    # 거리 저장
    check = list(inf for _ in range(v))
    check[x] = 0

    # 최단거리의 아직 방문하지 않은 점들 부터 탐색해나가기 위해 거리정보를 앞에 저장한다.
    hq = [[0, x]]
    heapq.heapify(hq)
    while hq:
        w, n = heapq.heappop(hq)
        if w > save[0]:
            save = [w, n]
        for b in bridge[n]:
            if check[b[1]] == inf:
                check[b[1]] = min(check[b[1]], b[0]+w)
                heapq.heappush(hq, [check[b[1]], b[1]])
            # check의 값이 업데이트 된 점의 경우에는 이미 hq에 추가되어 있기 때문에 다시 추가하지 않는다.
            else:
                check[b[1]] = min(check[b[1]], b[0]+w)

    return save


# 반드시 1부터 탐색해야할 필요는 없다. 어떤 Node 부터 탐색하더라도 결과는 같다.
x = bfs_far(1)
print(bfs_far(x[1])[0])
