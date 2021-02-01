import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def find(a):
    if a == elem_list[a]:
        return a
    elem_list[a] = find(elem_list[a])
    return elem_list[a] 
    
def merge(a,b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    if level[root_a] >= level[root_b]:
        elem_list[root_b] = root_a
        if level[root_a] == level[root_b]:
            level[root_a] += 1
    else:
        elem_list[root_a] = root_b

n,m = map(int,read().split())
elem_list = list(i for i in range(n+1))
level = list(1 for _ in range(n+1))

for _ in range(m):
    command, a, b = map(int,read().split())
    if command:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
    else:
        merge(a,b)
