import sys
read=sys.stdin.readline
from collections import deque

for _ in range(int(read())):    
    n = int(read())
    start = list(map(int,read().split()))
    end = list(map(int,read().split()))
    if start == end: 
        print(0)
        continue 
    MAP = list(list(1 for _ in range(n)) for _ in range(n))
    MAP[start[0]][start[1]] = 0
    point = deque([start])
    time = 1
    flag = 1
    while point and flag == 1:
        for _ in range(len(point)):
            a,b = point.popleft()
            for x,y in [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,-1),(2,1)]:
                ax, by = a+x, b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]:
                    if [ax,by] == end:
                        print(time)
                        flag = 2
                        break
                    point.append((ax,by))
                    MAP[ax][by] = 0
            if flag == 2:
                break

        time+=1
