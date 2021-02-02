import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def find(a):
    if a == union[a]:
        return a
    union[a] = find(union[a])
    return union[a]

def merge(a,b):
    root_a,root_b = find(a), find(b)
    if root_a == root_b:
        return
    if level[root_a] >= level[root_b]:
        if level[root_a] == level[root_b]:
            level[root_a] += 1
        union[root_b] = root_a
        count[root_a] += count[root_b]
    else:
        union[root_a] = root_b
        count[root_b] += count[root_a]
    return

def get_count(a):
    return count[find(a)]

for _ in range(int(read())):
    n = int(read())
    union = list(i for i in range(2*n+1))
    level = list(1 for _ in range(2*n+1))
    count = list(1 for _ in range(2*n+1))

    name = dict()
    cnt = 0
    
    for _ in range(n):
        a,b = read().split()
        if a not in name:
            cnt += 1
            name[a] = cnt
        a = name[a]

        if b not in name:
            cnt += 1
            name[b] = cnt
        b = name[b]

        merge(a,b)
        print(get_count(a))