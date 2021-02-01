import sys
read=sys.stdin.readline

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

n = int(read())
m = int(read())

union = list(i for i in range(n+1))
level = list(1 for _ in range(n+1))
link = list(list(map(int,read().split())) for _ in range(n))
travel = list(map(int,read().split()))
for i in range(m):
    travel[i] -= 1

for i in range(n):
    for j in range(i+1,n):
        if link[i][j]:
            merge(i,j)

for i in range(m-1):
    if find(travel[i]) != find(travel[i+1]):
        print("NO")
        break
else:
    print("YES")
