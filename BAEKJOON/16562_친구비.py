import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

import heapq as hq

def find(a):
    if a == union[a]:
        return a
    union[a] = find(union[a])
    return union[a]

def merge(a,b):
    root_a,root_b = find(a),find(b)
    if root_a == root_b:
        return
    if level[root_a]>=level[root_b]:
        if level[root_a]==level[root_b]:
            level[root_a] += 1
        union[root_b] = root_a
    else:
        union[root_a] = root_b
    return

n,m,k = map(int,read().split())
union = list(i for i in range(n+1))
level = list(1 for _ in range(n+1))
friend_cost = list((x,index+1) for index,x in enumerate(map(int,read().split())))

hq.heapify(friend_cost)

tot_cost = 0

for _ in range(m):
    a,b = map(int,read().split())
    merge(a,b)


friend_root = set()
while friend_cost:
    cost,i = hq.heappop(friend_cost)
    #print(cost, i, find(i))
    i_root = find(i)
    if i_root not in friend_root:
        friend_root.add(i_root)
        tot_cost += cost

    if tot_cost > k:
        break

if tot_cost > k:
    print("Oh no")
else:
    print(tot_cost)

        