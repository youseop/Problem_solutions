import sys
read=sys.stdin.readline
import heapq as hq

n = int(read())
h_o = list(sorted(map(int,read().split())) for _ in range(n))
h_o.sort(key = lambda x : -x[1])
length = int(read())
start_p = sorted(set(x[0] for x in h_o))

heap = []
hq.heapify(heap)
answer = 0
cnt = 0
for start in start_p:
    while h_o and h_o[-1][1] <= start + length:
        cnt += 1
        hq.heappush(heap, h_o.pop())
    while heap and heap[0][0] < start:
        hq.heappop(heap)
        cnt -= 1
    answer = max(cnt, answer)

print(answer)