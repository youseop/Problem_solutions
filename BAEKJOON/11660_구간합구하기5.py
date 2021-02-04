import sys
read=sys.stdin.readline

n,m = map(int,read().split())
MAP = [[0 for _ in range(n+1)]]+list([0]+list(map(int,read().split())) for _ in range(n))

for i in range(1,1+n):
    for j in range(1,1+n):
        MAP[i][j] += (MAP[i][j-1] + MAP[i-1][j] - MAP[i-1][j-1]) 

#for mm in MAP:
#    print(mm)
for _ in range(m):
    x1,y1,x2,y2 = map(int,read().split())
    print(MAP[x2][y2] - MAP[x1-1][y2] - MAP[x2][y1-1] + MAP[x1-1][y1-1])