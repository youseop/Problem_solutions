import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline
from heapq import heapify, heappush, heappop

def find(a):
    if a == union[a]:
        return a
    union[a] = find(union[a])
    return union[a]

def merge(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return

    if level[root_a] >= level[root_b]:
        if level[root_a] == level[root_b]:
            level[root_a] += 1
        union[root_b] = root_a
    else:
        union[root_a] = root_b
    return

def is_linked():
    if find(c) == find(v):
        return 1
    return 0

p,w = map(int,read().split())
c,v = map(int,read().split())
heap = []
union = list(i for i in range(p+1))
level = list(0 for _ in range(p+1))

for _ in range(w):
    a,b,dist = map(int,read().split())
    heappush(heap,(-dist,a,b))

while heap:
    dist,a,b = heappop(heap)
    dist *= (-1)
    merge(a,b)
    if is_linked():
        print(dist)
        break

