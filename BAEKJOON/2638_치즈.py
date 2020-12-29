import sys
from collections import deque
read=sys.stdin.readline
inf = sys.maxsize

#0이 저장되어 있는 공간(내부 공기)를 '*'(외부 공기)로 변경
def outside_air(a,b):
    MAP[a][b] = '*'
    point = deque([(a,b)])
    while point:
        a,b = point.popleft()
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax, by = a+x, b+y
            if MAP[ax][by] == 0:
                MAP[ax][by] = '*'
                point.append((ax,by))


def bfs():
    point = deque([])
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1:
                point.append((i,j))

    time = 0
    while point:
        #녹을 치즈들의 좌표를 저장
        isMelt = []
        for _ in range(len(point)):
            a,b = point.popleft()
            air = 0
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                ax,by = a+x, b+y
                if MAP[ax][by] == '*':
                    air+=1
                if air >=2:
                    isMelt.append((a,b))
                    #바로 '*'로 변경하게 되면 주변 점이 영향을 받게 된다.
                    #우선 0으로 변경 후, 한 사이클이 끝나고 내부공기와 함께 '*'로 변경
                    MAP[a][b] = 0
                    break
            #녹지 않았다면, 다음 사이클에 속할 수 있도록 deque에 다시 추가한다.
            else: point.append((a,b))

        if isMelt:
            #녹을 치즈들 주변의 내부 공기까지 모두 '*'으로 변경
            for a,b in isMelt:
                outside_air(a,b)
        time += 1
        
    return time

n,m = map(int,read().split())
MAP = list(list(map(int,read().split())) for _ in range(n))
outside_air(0,0)

print(bfs())