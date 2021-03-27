import sys
read = sys.stdin.readline


def find(a):
    if a == network[a]:
        return a
    network[a] = find(network[a])
    return network[a]


def merge(a,b):
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
city = {}
bridge = []

city_num = 0
for _ in range(n):
    x,y,weight = read().split()
    if x in city:
        x = city[x]
    else:
        city[x] = city_num
        x = city_num
        city_num += 1
    if y in city:
        y = city[y]
    else:
        city[y] = city_num
        y = city_num
        city_num += 1

    bridge.append((int(weight),x,y))

bridge.sort()

network = list(i for i in range(n))
level = list(0 for _ in range(n))
link_cnt = 0
total_cost = 0
for weight,x,y in bridge:
    if find(x) != find(y):
        merge(x,y)
        total_cost += weight
        link_cnt += 1
        if link_cnt == n:
            break

print(total_cost)
