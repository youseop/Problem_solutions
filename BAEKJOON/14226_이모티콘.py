import sys
read=sys.stdin.readline
from collections import deque

def bfs():
    cnt = 0
    check = set((0,1))
    point = deque([(0,1)])
    while point:
        for _ in range(len(point)):
            a,b = point.popleft()
            if (a,b) not in check: 
                if b == n:
                    return cnt
                if a != 0 and b != 1:
                    point.append((a,b-1))
                if a != 0 and b+a < 2*n:
                    point.append((a,b+a))
                if b != 0:
                    point.append((b,b))
            check.add((a,b))

        cnt += 1
    return cnt

n = int(read())
print(bfs())

