import sys
from collections import deque
read = sys.stdin.readline

f,s,g,u,d = map(int,read().split())
# 총 f층, 스타트링크는 g층, 강호는 지금 s층, u층위로 혹은 d층아래로

check = list(1 for _ in range(f+1))
check[s] = 0
point = deque([s])

def bfs():
    cnt = 0
    while point:
        for _ in range(len(point)):
            a = point.popleft()
            if a == g:
                return cnt
            for x in (u,-d):
                ax = a+x
                if 0<ax<=f and check[ax]:
                    check[ax] = 0
                    point.append(ax)
        cnt += 1
    return -1

res = bfs()
if res == -1:
    print('use the stairs')
else:
    print(res)