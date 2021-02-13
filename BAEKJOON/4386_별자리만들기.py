import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

from math import sqrt

def dist(a,b):
    ax,ay = float(a[0]),float(a[1])
    bx,by = float(b[0]),float(b[1])
    return sqrt((ax-bx)**2+(ay-by)**2)

def find(a):
    if a == network[a]:
        return a
    network[a] = find(network[a])
    return network[a]

def union(a,b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return
    network[root_a] = root_b

n = int(read())
xy = []
bridge = []
for _ in range(n):
    xy.append(list(read().split()))

for i in range(n):
    for j in range(i+1,n):
        bridge.append((dist(xy[i],xy[j]), i, j))

bridge.sort()
network = list(i for i in range(n))

answer = 0
for d,a,b in bridge:
    if find(a) != find(b):
        answer += d
        union(a,b)

print(round(answer,2))



