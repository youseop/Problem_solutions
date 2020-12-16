import sys, math
read=sys.stdin.readline
from collections import deque

def dfs(x,save,sum):
    if sum>n:
        return
    elif sum == n:
        answer.append(int(save))
        return

    for i in range(x+1,10):
        if sum+i<=n:
            dfs(i,save+str(i),sum+i)

N = int(read())
for _ in range(N):
    n = int(read())
    if n < 10:
        print(n)
        continue
    elif n > 45:
        print(-1)
        continue
    answer=[]
    dfs(0,"",0)
    print(min(answer))