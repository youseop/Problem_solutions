import sys
from collections import deque
read=sys.stdin.readline


def find(x,y):
    visit = list(1 for _ in range(10000))
    visit[x] = 0
    point = deque([x])
    time = 0
    while point:
        for _ in range(len(point)):
            ax = point.popleft()
            x1 = ax % 10
            x2 = (ax % 100)//10
            x3 = (ax%1000)//100
            x4 = ax // 1000
            if ax == b: return time
            for i in range(-x1,10-x1):
                a = ax + i
                if 1000<=a<10000 and unique[a] and visit[a]:
                    point.append(a)
                    visit[a] = 0
            for i in range(-x2*10,100-x2*10,10):
                a = ax + i
                if 1000<=a<10000 and unique[a] and visit[a]:
                    point.append(a)
                    visit[a] = 0
            for i in range(-x3*100,1000-x3*100,100):
                a = ax + i
                if 1000<=a<10000 and unique[a] and visit[a]:
                    point.append(a)
                    visit[a] = 0
            for i in range(-x4*1000,10000-x4*1000,1000):
                a = ax + i
                if 1000<=a<10000 and unique[a] and visit[a]:
                    point.append(a)
                    visit[a] = 0
        time += 1
    return 'Impossible'

unique = list(1 for _ in range(10000))
for i in range(2,100):
    if unique[i]:
        for j in range(2*i,10000,i):
            unique[j] = 0
            
for _ in range(int(read())):
    a,b = map(int,read().split())
    print(find(a,b))
