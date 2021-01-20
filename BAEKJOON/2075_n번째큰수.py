import sys
read=sys.stdin.readline
from heapq import heappush, heappop, heapify
n = int(read())

pointer = list(map(int,read().split()))
heapify(pointer)

for _ in range(n-1):
    for i in list(map(int,read().split())):
        heappush(pointer,i)
    for _ in range(n):
        heappop(pointer)

print(pointer[0])