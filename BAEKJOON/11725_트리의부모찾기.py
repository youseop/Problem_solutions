from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
bridge = dict()
for _ in range(n-1):
    a, b = map(int, read().split())
    if a in bridge:
        bridge[a].append(b)
    else:
        bridge[a] = [b]
    if b in bridge:
        bridge[b].append(a)
    else:
        bridge[b] = [a]
save = list(-1 for _ in range(n+1))
save[1] = 0
point = deque([1])

while point:
    a = point.popleft()
    for i in bridge[a]:
        if save[i] == -1:
            save[i] = a
            point.append(i)
for i in save[2:]:
    print(i)
