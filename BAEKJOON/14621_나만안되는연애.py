import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def find(a):
    if network[a] == a:
        return a
    network[a] = find(network[a])
    return network[a]

def union(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return
    network[root_a] = root_b

n,m = map(int,read().split())
MorW = list(read().split())
network = list(i for i in range(n))
bridge = [list(map(int,read().split())) for _ in range(m)]
bridge.sort(key = lambda x: x[2])

distance = 0
cnt = 1
for a,b,d in bridge:
    a,b = a-1,b-1
    if MorW[a] == MorW[b]: continue
    if find(a) != find(b):
        distance += d
        union(a,b)
        cnt += 1

if cnt == n: print(distance)
else: print(-1)