import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque

def getRect(left,right,top,down):
    deq = deque()
    for i in range(down-top):
        deq.append(arr[top+i][left])
    for i in range(right-left):
        deq.append(arr[down][left+i])
    for i in range(down-top):
        deq.append(arr[down-i][right])
    for i in range(right-left):
        deq.append(arr[top][right-i])
    return deq

def putRect(deq,left,right,top,down):
    cnt = 0
    for i in range(down-top):
        arr[top+i][left] = deq[cnt]
        cnt += 1
    for i in range(right-left):
        arr[down][left+i] = deq[cnt]
        cnt += 1
    for i in range(down-top):
        arr[down-i][right] = deq[cnt]
        cnt += 1
    for i in range(right-left):
        arr[top][right-i] = deq[cnt]
        cnt += 1



n,m,r = map(int,read().split())
arr = list(list(map(int,read().split())) for _ in range(n))

for i in range(min(n//2,m//2)):
    left,right,top,down = i,m-1-i,i,n-1-i
    T = r%(2*(n-1+m-1-4*i))
    deq = getRect(left,right,top,down)
    deq.rotate(T)
    putRect(deq,left,right,top,down)

for a in arr:
    print(*a)