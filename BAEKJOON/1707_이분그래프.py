from collections import deque
import sys
read = sys.stdin.readline


def BFS(x):
    point = deque([x])
    if check[x] == 0:
        check[x] = 1
    else:
        return True
    flag = 1
    while point and flag == 1:
        a = point.popleft()
        if a in bridge:
            for b in bridge[a]:
                if check[b] == 0:
                    if check[a] == 1:
                        check[b] = 2
                    else:
                        check[b] = 1
                    point.append(b)
                elif check[a] == check[b]:
                    flag = 2
    if flag == 2:
        return False
    else:
        return True


for _ in range(int(read())):
    v, e = map(int, read().split())
    bridge = dict()
    for _ in range(e):
        a, b = map(int, read().split())
        if a in bridge:
            bridge[a].append(b)
        else:
            bridge[a] = [b]
        if b in bridge:
            bridge[b].append(a)
        else:
            bridge[b] = [a]

    check = list(0 for _ in range(v+1))
    for i in range(1, v+1):
        if not BFS(i):
            print("NO")
            break
    else:
        print("YES")
