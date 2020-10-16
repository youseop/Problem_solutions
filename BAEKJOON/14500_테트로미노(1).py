import sys
read=sys.stdin.readline

n,m=map(int,read().split())
block=list(list(map(int,read().split())) for _ in range(n))

aws=-2147000000
dx=[0,1,0,-1]
dy=[1,0,-1,0]

check=list(list(True for _ in range(m)) for _ in range(n))


def dfs(a,b,save,count):
    global aws
    if count==4:
        aws=max(aws,save)
        return
    for x,y in zip(dx,dy):
        if 0<=a+x<n and 0<=b+y<m and check[a+x][b+y]:
            check[a+x][b+y]=False
            dfs(a+x,b+y,save+block[a+x][b+y],count+1)
            check[a+x][b+y]=True
    return

etc=[[[0,0],[0,1],[0,2],[1,1]],[[0,0],[0,1],[0,2],[-1,1]],[[0,0],[1,0],[2,0],[1,1]],[[0,0],[1,0],[2,0],[1,-1]]]

def dfs_etc(a,b):
    global aws
    for xy in etc:
        sum=0
        for x,y in xy:
            if 0<=a+x<n and 0<=b+y<m:
                sum+=block[a+x][b+y]
            else: break
        else: aws=max(aws,sum)
    return

for i in range(n):
    for j in range(m):
        dfs(i,j,0,0)
        dfs_etc(i,j)
print(aws)