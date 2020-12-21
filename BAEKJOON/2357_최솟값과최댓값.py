import sys
read=sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = [num[start], num[start]]
        return tree[node]
    mid = (start+end)//2
    a_max,a_min= init(start,mid,node*2)
    b_max,b_min= init(mid+1,end,node*2+1)
    tree[node] = [max(a_max,b_max), min(a_min,b_min)]
    return tree[node]

def tree_max(start, end, node, left, right):
    if left > end or right < start:
        return [0, sys.maxsize]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)//2
    a_max, a_min = tree_max(start, mid, node*2, left, right)
    b_max, b_min = tree_max(mid+1, end, node*2+1, left, right)
    return [max(a_max,b_max), min(a_min,b_min)]

n, m = map(int,read().split())
num = list(int(read()) for _ in range(n))
tree = list( 0 for _ in range(4*n))
init(0, n-1, 1)
for _ in range(m): 
    a, b = map(int,read().split())
    print(*tree_max(0,n-1,1,a-1,b-1)[::-1])