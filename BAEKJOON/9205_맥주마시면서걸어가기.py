import sys
read=sys.stdin.readline

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def dfs(index,visit):
    global flag
    if flag:
        return
    elif index == n-1:
        print('happy')
        flag = 1
        return
    for i in range(n):
        if visit | (1<<i) != visit and visited[i] and distance(place[i],place[index])<=1000:
            visited[i] = 0
            dfs(i, visit|(1<<i))
        

for _ in range(int(read())):
    flag = 0
    n = int(read())
    place = []
    place.append(list(map(int,read().split())))
    for _ in range(n):
        place.append(list(map(int,read().split())))
    place.append(list(map(int,read().split())))
    n+=2
    visited=[1 for _ in range(n)]
    visited[0] = 0
    dfs(0, 0)
    if flag == 0:
        print('sad')