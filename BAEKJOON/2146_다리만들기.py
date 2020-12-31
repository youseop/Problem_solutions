import sys
from collections import deque
read=sys.stdin.readline

def bfs(i,j,cnt_town):
    town_cand = []
    point = deque([(i,j)])
    MAP[i][j] = cnt_town
    while point:
        a,b = point.popleft()
        town_cand.append((a,b))
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax, by = a+x, b+y
            if 0<=ax<n and 0<=by<n and MAP[ax][by] == 1:
                MAP[ax][by] = cnt_town
                point.append((ax,by))

    towns.append(town_cand)
    return

def find(numb):
    point = deque(town)
    visit = list(list(1 for _ in range(n)) for _ in range(n))
    time = -1
    while point:
        for _ in range(len(point)):
            a,b = point.popleft()
            if MAP[a][b] != 0 and MAP[a][b] != numb:
                return time
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                ax, by = a+x, b+y
                if 0<=ax<n and 0<=by<n \
                    and visit[ax][by] \
                    and MAP[ax][by] != numb:

                    visit[ax][by] = 0
                    point.append((ax,by))
        time += 1

n = int(read())
MAP = list(list(map(int,read().split())) for _ in range(n))
cnt_town = -1
towns = []
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            bfs(i,j,cnt_town)
            cnt_town -= 1

answer = 2417000000
for town in towns:
    a,b = town[0]
    numb = MAP[a][b]
    answer = min(answer,find(numb))

print(answer)