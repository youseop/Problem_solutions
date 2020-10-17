from collections import deque
import sys
read = sys.stdin.readline

n, m, k, x = map(int, read().split())
city = dict()
for _ in range(m):
    a, b = map(int, read().split())
    if a in city:
        city[a].append(b)
    else:
        city[a] = [b]
# print(city)
# n - #city
# m - #road
# k - how far
# x - start from

save = deque([x])

check = list(-1 for _ in range(n))
check[x-1] = 0
answer = []

while save:
    a = save.popleft()
    if a in city:
        for c in city[a]:
            if check[c-1] == -1:
                save.append(c)
                check[c-1] = check[a-1]+1
                if check[c-1] == k:
                    answer.append(c)

if answer:
    answer.sort()
    for a in answer:
        print(a)

else:
    print(-1)
