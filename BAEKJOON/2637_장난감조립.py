import sys
from collections import deque
read=sys.stdin.readline

n = int(read())

need = list([] for _ in range(n+1)) #특정 부품을 필요로 하는 중간 부품&완제품의 번호 저장
parts = list(dict() for _ in range(n+1)) #장난감을 조립하는데 필요한 파츠들 각각의 개수
check = list(0 for _ in range(n+1)) #아직 완료되지 않은 중간 부품의 개수

for _ in range(int(read())):
    x,y,k = map(int,read().split())
    parts[x][y] = k
    need[y].append(x)

for i in range(1,n+1):
    for j in parts[i].keys():
        if parts[j]:
            check[i] += 1

point = deque([])
for i in range(1,n+1):
    if check[i] == 0:
        point.append(i)

while point:
    a = point.popleft()
    if not parts[a]: continue
    for i in need[a]:
        for j in parts[a].keys():
            if j not in parts[i]:
                parts[i][j] = parts[a][j] * parts[i][a]
            else:
                parts[i][j] += parts[a][j] * parts[i][a]
        del parts[i][a]
        check[i] -= 1
        if check[i] == 0:
            point.append(i)


for i in sorted(parts[n].keys()):
    print(i,parts[n][i])