import sys
read = sys.stdin.readline

from collections import deque

def bfs(s_x,s_y):
    point = deque([(s_x,s_y)])
    while point:
        a,b = point.popleft()
        if a==e_x and b==e_y:
            return MAP[a][b]
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            for i in range(1,k+1):
                ax,by = a+x*i,b+y*i
                if not (0<=ax<n and 0<=by<m) or MAP[ax][by] == '#':
                  break
                if MAP[ax][by] == '.':
                    MAP[ax][by] = MAP[a][b]+1
                    point.append((ax,by))
                elif MAP[ax][by]==MAP[a][b]+1:
                    continue
                else:
                    break
    return -1

n,m,k = map(int,read().split())
MAP = list(list(read().strip()) for _ in range(n))
s_x,s_y,e_x,e_y = map(lambda x: int(x)-1,read().split())
MAP[s_x][s_y] = 0
answer = bfs(s_x,s_y)
print(answer)