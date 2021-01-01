import sys
read=sys.stdin.readline
from collections import deque

n,k = map(int,read().split()) # n - 멀티탭 구멍 개수
num = deque(map(int,read().split()))
pluged = set()

while len(pluged)<n:
    pluged.add(num.popleft())

soon = list(deque([]) for _ in range(k+1))
for i in range(len(num)):
    soon[num[i]].append(i)
for i in range(k+1):
    soon[i].append(2147000000)

cnt = 0
for i in range(len(num)):
    x = num[i]
    soon[x].popleft()
    if x in pluged: 
        continue
    cnt += 1
    a = max(list(i for i in pluged), key=lambda x : soon[x][0])
    pluged.remove(a)
    pluged.add(x)
print(cnt)