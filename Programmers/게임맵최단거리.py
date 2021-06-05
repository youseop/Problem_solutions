from collections import deque

def solution(maps):
    n,m = len(maps),len(maps[0])
    end_point = (n-1,m-1)
    point = deque([[0,0]])    
    time = 1
    while point:
        print(point)
        for _ in range(len(point)):
            if point[0] == end_point:
                return time
            a,b = point.popleft()
            for x,y in ((0,1),(1,0),(0,-1),(-1,0)):
                ax,by = a+x,b+y
                if 0<=ax<n and 0<=by<m and maps[ax][by]:
                    maps[ax][by] = 0
                    point.append((ax,by))
            
        time += 1
    return -1