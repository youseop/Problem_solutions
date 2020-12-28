import sys
from collections import deque
read=sys.stdin.readline
inf = sys.maxsize
n,m = map(int,read().split())
MAP = list(list(int(i) for i in read().strip()) for _ in range(n))

def BFS():
    check = list(list([inf,inf] for _ in range(m)) for _ in range(n))

    point = deque([(0,0,0)])  #break_wall, x, y
    check[0][0] = [1,inf]

    while point:
        b_w, a, b = point.popleft()
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            ax, by = a+x, b+y
            if 0<=ax<n and 0<=by<m:
                if b_w == 0:
                    if MAP[ax][by] and check[ax][by][1] > check[a][b][0]+1:
                        check[ax][by][1] = check[a][b][0]+1
                        point.append((1, ax, by))

                    elif MAP[ax][by]==0 and check[a][b][0]+1<check[ax][by][0]:
                        check[ax][by][0] = check[a][b][0]+1
                        point.append((0, ax, by))

                elif MAP[ax][by]==0 and b_w == 1 and check[a][b][1]+1<check[ax][by][1]:
                    check[ax][by][1] = check[a][b][1]+1
                    point.append((1, ax, by))

    answer = min(check[-1][-1])
    if answer == inf:
        print(-1)
    else:
        print(answer)
BFS()

##########################################################

import sys
read=sys.stdin.readline
inf = sys.maxsize

def BFS():
    visit = [[1]*m for _ in range(n)]
    visit_break = [[1]*m for _ in range(n)]
    visit[0][0] = 0
    visit_break[0][0] = 0
    point = [(0,0,0)]  #break wall, x, y
    cnt = 1
    while point:
        point_ = []
        for b_w, a, b in point:
            if a == n-1 and b == m-1:
                return cnt
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                ax, by = a+x, b+y
                if 0<=ax<n and 0<=by<m:
                    if b_w:
                        if visit_break[ax][by] and MAP[ax][by]==0:
                            visit_break[ax][by] = 0
                            point_.append((1, ax, by))                         

                    else:
                        if visit[ax][by] and MAP[ax][by] == 0:
                            visit[ax][by] = 0
                            point_.append((0, ax, by))
                        elif visit[ax][by] and MAP[ax][by] == 1:
                            visit[ax][by] = 0
                            point_.append((1, ax, by))
        point = point_
        cnt += 1
    return -1

n,m = map(int,read().split())
MAP = [list(int(i) for i in read().strip()) for _ in range(n)]
print(BFS())