import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

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


n,m = map(int,read().split())
network = list(i for i in range(n+1))
level = list(0 for i in range(n+1))
answer = 0

bridge = list(list(map(int,read().split())) for _ in range(m))
bridge.sort(key = lambda x: x[2])

for a,b,dist in bridge:
    if find(a) == find(b):
        continue
    answer += dist
    union(a,b)

print(answer)

