import sys
read=sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    mid = (start + end)//2
    tree[node] = init(start, mid, node*2) + init(mid + 1, end, node*2+1)
    return tree[node]

def tree_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)//2
    return tree_sum(start, mid, node*2, left, right) + tree_sum(mid + 1, end, node*2+1, left, right)

def update(start,end,node,index,diff):
    if index < start or index > end:
        return
    
    tree[node] += diff

    if start != end:
        mid = (start + end)//2
        update(start, mid ,node*2, index, diff)
        update(mid+1, end ,node*2+1, index, diff)


n,m,k=map(int,read().split())

a=list(int(read()) for _ in range(n))
tree = [0]*(4*n)

init(0,n-1,1)

for _ in range(m+k):
    x,y,z=map(int,read().split())
    if x == 1:
        y-=1
        diff = z - a[y]
        a[y] = z
        update(0,n-1,1,y,diff)
    else:
        print(tree_sum(0,n-1,1,y-1,z-1))

