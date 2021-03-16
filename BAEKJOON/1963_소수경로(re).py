import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

from collections import deque

def bfs(start,end):
    point = deque([start])
    check = decimal[::]
    cnt = 0
    while point:
        for _ in range(len(point)):
            a = point.popleft()
            if a == end:
                return cnt
            for i in range(4):
                for j in range(10):
                    tmp = list(str(a))
                    tmp[i] = str(j)
                    tmp = int("".join(tmp))
                    if 1000<=tmp<10000 and check[tmp]:
                        point.append(tmp)
                        check[tmp] = 0
        cnt += 1
    return 'Impossible'


decimal = list(1 for _ in range(10000))
for i in range(2,101):
    if decimal[i]:
        for j in range(i*2,10000,i):
            decimal[j] = 0

for _ in range(int(read())):
    a,b = map(int,read().split())
    print(bfs(a,b))