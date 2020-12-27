import sys
from collections import deque
read=sys.stdin.readline
inf = sys.maxsize
n,m = map(int,read().split())
MAP = list(list(int(i) for i in read().strip()) for _ in range(n))

def BFS():
    check = list(list([inf,inf] for _ in range(m)) for _ in range(n))

    point = deque([(0,0,0)])  #break wall, x, y
    check[0][0] = [1,1]

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