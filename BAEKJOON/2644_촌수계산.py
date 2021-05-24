import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque


def bfs():
    cnt = 0
    point = deque([s])
    check = list(1 for _ in range(n+1))
    check[s] = 0
    while point:
        for _ in range(len(point)):
            a = point.popleft()
            if a == e:
                return cnt
            for x in bridge[a]:
                if check[x]:
                    check[x] = 0
                    point.append(x)
        cnt += 1
    return -1


n = int(read())
s,e = map(int,read().split())
bridge = list([] for _ in range(n+1))
for _ in range(int(read())):
    a,b = map(int,read().split())
    bridge[a].append(b)
    bridge[b].append(a)

print(bfs())



'''
import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque

n = int(read())
a,b = map(int,read().split())

bridge = list([] for _ in range(n+1))

for _ in range(int(read())):
    x,y = map(int,read().split())
    bridge[x].append(y)
    bridge[y].append(x)

point = deque([a])
count = 0
check = list(True for _ in range(n+1))
while point:
    for _ in range(len(point)):
        p = point.popleft()
        if p == b:
            print(count)
            exit()

        for next_p in bridge[p]:
            if check[next_p]:
                check[next_p] = False
                point.append(next_p)

    count += 1

print(-1)
'''