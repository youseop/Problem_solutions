import sys
read=sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = min(init(start,mid,node*2), init(mid+1,end,node*2+1))
    return tree[node]

def tree_max(start, end, node, left, right):
    if left > end or right < start:
        return sys.maxsize
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)//2
    return min(tree_max(start, mid, node*2, left, right), tree_max(mid+1, end, node*2+1, left, right))

n, m = map(int,read().split())
num = list(int(read()) for _ in range(n))
tree = list( 0 for _ in range(4*n))
init(0, n-1, 1)
for _ in range(m): 
    a, b = map(int,read().split())
    print(tree_max(0,n-1,1,a-1,b-1))