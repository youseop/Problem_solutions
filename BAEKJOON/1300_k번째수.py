import sys
import math
read=sys.stdin.readline

def find(x):
    cnt = 0
    for i in range(1,min(x,n)+1):
        cnt += min(n,x//i)
    return cnt

n = int(read())
k = int(read())

l,r = 1,n*n
while l<=r:
    mid = (l+r)//2
    if find(mid) < k:
        l = mid + 1
    else :
        r = mid - 1
        save = mid

print(save)