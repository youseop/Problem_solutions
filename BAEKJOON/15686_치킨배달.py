from collections import deque
import sys
read = sys.stdin.readline
answer = sys.maxsize
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

n, m = map(int, read().split())
MAP = list(list(map(int, read().split())) for _ in range(n))

# 치킨집과 집들의 좌표 저장
chicken = dict()
house = dict()
# dictionary에 치킨집과 집들을 0번부터 번호를 매기기 위해 사용
cnt_chicken = -1
cnt_house = -1

for i in range(n):
    for j in range(n):
        if MAP[i][j] == 2:
            cnt_chicken += 1
            chicken[cnt_chicken] = (i, j)
        if MAP[i][j] == 1:
            cnt_house += 1
            house[cnt_house] = (i, j)

# 치킨집을 m개만큼 골라낸후, 치킨거리의 최소값을 answer에 저장한다.


def DFS(chicken_list, index, count):
    global answer
    if count == m:
        answer = min(answer, DIST(chicken_list))
    else:
        for i in range(index, cnt_chicken+1):
            DFS(chicken_list+[i], i+1, count+1)

# 골라진 m개의 치킨집에 대해 각각의 집들로 부터의 치킨 거리를 구한다.


def DIST(chicken_list):
    dist_sum = 0

    for j in range(cnt_house+1):
        a, b = house[j]
        dist = sys.maxsize
        for i in chicken_list:
            x, y = chicken[i]
            dist = min(dist, abs(x-a)+abs(y-b))
        dist_sum += dist

    return dist_sum


DFS([], 0, 0)
print(answer)
