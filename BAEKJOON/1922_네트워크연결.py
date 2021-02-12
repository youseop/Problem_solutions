import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline
import heapq as hq

def find(a):
    if a == network[a]:
        return a
    network[a] = find(network[a])
    return network[a]

def union(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return
    if level[root_a] >= level[root_b]:
        if level[root_a] == level[root_b]:
            level[root_a] += 1
        network[root_b] = root_a
    else:
        network[root_a] = root_b


n = int(read())
m = int(read())
network = list(i for i in range(n))
level = list(0 for i in range(n))
bridge = []
answer = 0

for _ in range(m):
    a,b,c = map(int,read().split())
    if a==b: continue
    hq.heappush(bridge,(c,a-1,b-1))


while bridge:
    dist,a,b = hq.heappop(bridge)
    if find(a) == find(b):
        continue
    answer += dist
    union(a,b)

print(answer)

