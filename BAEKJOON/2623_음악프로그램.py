from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
bridge = dict()
left_num = list(0 for _ in range(n+1))

for _ in range(m):
    tmp = list(map(int, read().split()))
    for i in range(1, tmp[0]):
        if tmp[i] not in bridge:
            bridge[tmp[i]] = [tmp[i+1]]
        else:
            bridge[tmp[i]].append(tmp[i+1])
        left_num[tmp[i+1]] += 1
point = deque([])
for i in range(1, n+1):
    if left_num[i] == 0:
        point.append(i)

answer = []
while point:
    a = point.popleft()
    answer.append(a)
    if a in bridge:
        for i in bridge[a]:
            left_num[i] -= 1
            if left_num[i] == 0:
                point.append(i)

if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)
