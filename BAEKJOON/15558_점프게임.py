import sys
from collections import deque
read=sys.stdin.readline

n,k=map(int,read().split())

MAP=list(list(map(int,read().strip())) for _ in range(2))
check=list(list(True for _ in range(n)) for _ in range(2))

point=deque([[0,0]])
check[0][0]=False

cnt=-1

while point:
    cnt+=1
    for _ in range(len(point)):
        a,b=point.popleft()
        if cnt>b:continue

        if b>=n-1 or b+k>=n:
            print(1)
            sys.exit()

        if MAP[a][b+1] == 1 and check[a][b+1]:
            point.append([a,b+1])
            check[a][b+1]=False

        if b-1>=0 and MAP[a][b-1] == 1 and check[a][b-1]:
            point.append([a,b-1])
            check[a][b-1]=False

        if a==1:
            if b+k<n and MAP[0][b+k]==1 and check[0][b+k]:
                point.append([0,b+k])
                check[0][b+k]=False

        if a==0:
            if b+k<n and MAP[1][b+k]==1 and check[1][b+k]:
                point.append([1,b+k])
                check[1][b+k]=False
    

print(0)


