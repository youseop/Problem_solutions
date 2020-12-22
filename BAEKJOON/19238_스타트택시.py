##한 달 만에 드디어 풀었습니다 ㅠㅠ##
import sys
read=sys.stdin.readline
from collections import deque

dx=[-1,0,0,1]
dy=[0,-1,1,0]

n,m,fuel = map(int,read().split())
MAP=list(list(map(int,read().split())) for _ in range(n))
start = list(map(int,read().split()))
start[0],start[1]=start[0]-1,start[1]-1
get=list(list([] for _ in range(n)) for _ in range(n))
for _ in range(m):
    a,b,c,d=map(int,read().split())
    get[a-1][b-1].append([c-1,d-1])

def find_pas(start):
    global fuel
    if get[start[0]][start[1]]:
        return ([start[0],start[1]],get[start[0]][start[1]].pop())

    point=deque([start])
    check=list(list(True for _ in range(n)) for _ in range(n))
    check[start[0]][start[1]]=False
    while point:
        point = deque(sorted(point))
        for _ in range(len(point)):
            a,b=point.popleft()
            ##여기서 체크해줘야 한다!!!!
            if get[a][b]:
                return ([a,b],get[a][b].pop())
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    check[ax][by]=False
                    point.append([ax,by])
        fuel-=1
        if fuel < 0:
            return 0, 0
    return 0, 0

def go_pas(start,end):
    global fuel
    if start == end:
        return
    point=deque([start])
    check=list(list(True for _ in range(n)) for _ in range(n))
    check[start[0]][start[1]]=False
    far=0
    while point:
        for _ in range(len(point)):
            a,b=point.popleft()
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    check[ax][by]=False
                    point.append([ax,by])
                    if [ax,by]==end:
                        fuel += (far+1)
                        return 1
        far+=1
        if far >= fuel:
            return 0
    return 0

for _ in range(m):
    f, t=find_pas(start)
    if f:
        if go_pas(f,t) == 0:
            print(-1)
            break
    else:
        print(-1)
        break
    start = t
else:
    print(fuel)




# BFS와 DFS에 대해 더 공부해야겠다...
# Solved X
'''
import sys
sys.stdin = open("input.txt","rt")
read=sys.stdin.readline

n,m,fuel=map(int,read().split())
MAP=list(list(map(int,read().split())) for _ in range(n))
x,y=map(int,read().split())
tmp=list(list(map(int,read().split())) for _ in range(m))
FromTo=list(list([] for _ in range(n)) for _ in range(n))
for t in tmp:
    if FromTo[t[0]-1][t[1]-1]: FromTo[t[0]-1][t[1]-1].append([t[2]-1,t[3]-1])
    else: FromTo[t[0]-1][t[1]-1]=[[t[2]-1,t[3]-1]]


dx=[-1,0,1,0]
dy=[0,-1,0,1]

from collections import deque

def find_person():
    if len(bfs)==0:
        print(-1)
        sys.exit()
    a,b=bfs.popleft()
    if FromTo[a][b]:
        tmp=FromTo[a][b].pop()
        return [[a,b],tmp,check[a][b]]

    for da,db in zip(dx,dy):
        X=a+da
        Y=b+db
        if 0<=X<n and 0<=Y<n and MAP[X][Y]==0 and check[X][Y]==0:
            check[X][Y]=check[a][b]+1
            bfs.append([X,Y])
    
    return find_person()



def find_distance(tox,toy):
    if len(bfs_d)==0:
        print(-1)
        sys.exit()
    a,b=bfs_d.popleft()
    if a == tox and b==toy:
        return check[a][b]
    for da,db in zip(dx,dy):
        X=a+da
        Y=b+db
        if 0<=X<n and 0<=Y<n and MAP[X][Y]==0 and check[X][Y]==0:
            check[X][Y]=check[a][b]+1
            bfs_d.append([X,Y])
    return find_distance(tox,toy)

bfs=deque([[x-1,y-1]])
for _ in range(m):
    check=list(list(0 for _ in range(n)) for _ in range(n))
    aa,bb,d_1=find_person()
    #print(aa,bb,d_1)

    check=list(list(0 for _ in range(n)) for _ in range(n))
    bfs_d=deque([[aa[0],aa[1]]])
    d_2=find_distance(bb[0],bb[1])
    bfs=deque([[bb[0],bb[1]]])
    if d_1+d_2>fuel:
        print(-1)
        sys.exit()
    else: fuel=fuel-d_1+d_2
print(fuel)
'''
# 두번째시도,,, 왜이렇게 풀릴듯 하면서 안풀리는지 모르겠다.
'''
import sys
read = sys.stdin.readline
from collections import deque
n, m, fuel = map(int, read().split())

MAP = list(list(map(int, read().split())) for _ in range(n))
a, b = list(map(int, read().split()))
start = [a-1, b-1]
pas = dict()
checkpas = dict()
for _ in range(m):
    a, b, c, d = map(int, read().split())
    pas[(a-1, b-1)] = (c-1, d-1)
    checkpas[(a-1, b-1)] = True

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def findPAS(start):
    check = list(list(True for _ in range(n)) for _ in range(n))
    point = deque([start])
    far = 0
    same_far = []
    while point:
        term = len(point)
        for _ in range(term):
            a, b = point.popleft()
            check[a][b] = False
            if (a, b) in pas and checkpas[(a, b)]:
                same_far.append([far, (a, b)])
            for x, y in zip(dx, dy):
                ax, by = a+x, b+y
                if 0 <= ax < n and 0 <= by < n and MAP[ax][by] == 0 and check[ax][by]:
                    point.append([ax, by])
        far += 1
        if far > fuel:
            break
        if same_far:
            same_far.sort(key=lambda x: (x[1][0], x[1][1]))
            return same_far[0]

    print(-1)
    sys.exit()
    return


def takePAS(a, b):
    check = list(list(True for _ in range(n)) for _ in range(n))
    c, d = pas[(a, b)]
    point = deque([[a, b]])
    far = 0
    while point:
        term = len(point)
        for _ in range(term):
            a, b = point.popleft()
            check[a][b] = False
            if c == a and d == b:
                return far
            for x, y in zip(dx, dy):
                ax, by = a+x, b+y
                if 0 <= ax < n and 0 <= by < n and MAP[ax][by] == 0 and check[ax][by]:
                    point.append([ax, by])
        far += 1
        if len_From+far > fuel:
            break
    print(-1)
    sys.exit()
    return


point = 0

for _ in range(m):
    len_From, point = findPAS(start)
    len_To = takePAS(point[0], point[1])

    if fuel < len_From+len_To:
        print(-1)
        sys.exit()

    fuel = fuel-len_From+len_To

    start = pas[point[0], point[1]]
    checkpas[(point[0], point[1])] = False

print(fuel)
'''
#세번째 시도...
#한 손님의 도착지가 다른 손님의 출발지인 경우
#택시의 출발지가 어떤 손님의 출발지와 겹치는 경우
#손님까지 도달하지 못하거나, 손님을 목적지까지 데려다드리지 못하는 경우
#고려했는데 아직 안된다...
'''
import sys
sys.stdin = open("TextFile1.txt","rt")
read=sys.stdin.readline
from collections import deque

dx=[-1,0,0,1]
dy=[0,-1,1,0]

n,m,fuel = map(int,read().split())
MAP=list(list(map(int,read().split())) for _ in range(n))
start = list(map(int,read().split()))
start[0],start[1]=start[0]-1,start[1]-1
#같은 출발지, 다른 도착지의 승객들이 있으면 어떻게?!
get=list(list([] for _ in range(n)) for _ in range(n))
for _ in range(m):
    a,b,c,d=map(int,read().split())
    get[a-1][b-1].append([c-1,d-1])

def find_pas(start):
    global fuel
    if get[start[0]][start[1]]:
        return ([start[0],start[1]],get[start[0]][start[1]].pop())

    point=deque([start])
    check=list(list(True for _ in range(n)) for _ in range(n))
    check[start[0]][start[1]]=False
    while point:
        point = deque(sorted(point))
        for _ in range(len(point)):
            a,b=point.popleft()
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    check[ax][by]=False
                    point.append([ax,by])
                    if get[ax][by]:
                        fuel-=1
                        return ([ax,by],get[ax][by].pop())
        fuel-=1
        if fuel <= 0:
            return 0
    return 0

def go_pas(start,end):
    global fuel
    if start == end:
        return
    point=deque([start])
    check=list(list(True for _ in range(n)) for _ in range(n))
    check[start[0]][start[1]]=False
    far=0
    while point:
        for _ in range(len(point)):
            a,b=point.popleft()
            for x,y in zip(dx,dy):
                ax,by=a+x,b+y
                if 0<=ax<n and 0<=by<n and MAP[ax][by]==0 and check[ax][by]:
                    check[ax][by]=False
                    point.append([ax,by])
                    if [ax,by]==end:
                        fuel += (far+1)
                        return 1
        far+=1
        if far >= fuel:
            return 0
    return 0

for _ in range(m):
    tmp=find_pas(start)
    print(fuel)
    if tmp:
        f,t=tmp
        print(f,t)
        if go_pas(f,t) == 0:
            print(-1)
            break
        print(fuel)
    else:
        print(-1)
        break

    start = t
else:
    print(fuel)

    
    
'''