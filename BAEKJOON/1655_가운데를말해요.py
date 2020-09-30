import sys
import heapq
n = int(input())
up = []
down = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if not down:
        heapq.heappush(down, -num)
    else:
        if -down[0] >= num:
            heapq.heappush(down, -num)
        else:
            heapq.heappush(up, num)
    if len(down)-len(up) == 2:
        tmp = -heapq.heappop(down)
        heapq.heappush(up, tmp)
    elif len(down) < len(up):
        tmp = -heapq.heappop(up)
        heapq.heappush(down, tmp)

    print(-down[0])
