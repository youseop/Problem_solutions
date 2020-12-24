import sys
read=sys.stdin.readline
import heapq as hq
    
K, N = map(int,read().split())
prime = list(map(int,read().split()))
if K == 1:
    print(prime[0]**N)
    exit()

num=list((prime[i], i) for i in range(K))
max_num = list(-prime[i] for i in range(K))
hq.heapify(num)
hq.heapify(max_num)

for x in range(N):
    num_pop, index = hq.heappop(num)
    for i in range(index, K):
        if len(max_num) >= N and -max_num[0] <= num_pop*prime[i]:
            continue
        hq.heappush(num, (num_pop*prime[i], i))
        hq.heappush(max_num, -num_pop*prime[i])

print(num_pop)
