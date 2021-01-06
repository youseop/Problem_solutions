import sys
read=sys.stdin.readline

n = int(read())
MAP = list(list(map(lambda x: -int(x),read().split())) for _ in range(n))
MAP[-1][-1] = 1

def dfs(a,b):
    if MAP[a][b] >= 0:
        return MAP[a][b]
    distance = -MAP[a][b]
    MAP[a][b] = 0
    if a+distance < n and MAP[a+distance][b]!=0:
        MAP[a][b] += dfs(a+distance,b)
    
    if b+distance < n and MAP[a][b+distance]!=0:
        MAP[a][b] += dfs(a,b+distance)

    return MAP[a][b]       

dfs(0,0)
print(MAP[0][0])