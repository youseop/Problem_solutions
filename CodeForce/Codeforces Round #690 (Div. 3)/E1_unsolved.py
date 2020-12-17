import sys, math
read=sys.stdin.readline
from collections import deque

def triple(cnt,save,minimum):
    global answer
    if cnt == 3:
        answer += 1
        return
    for i in range(save+1,n-2+cnt):
        if num[i]-minimum<=2:
            triple(cnt+1,i,minimum)
    return

N = int(read())
for _ in range(N):
    n = int(read())
    num=list(map(int,read().split()))
    if n <3:
        print(0)
        continue
    num.sort()
    answer = 0
    for i in range(n-2):
        triple(1,i,num[i])
    print(answer)

