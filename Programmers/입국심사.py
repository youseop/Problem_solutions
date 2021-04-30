import sys

def getThroughput(total_time, times):
    cnt = 0
    for t in times:
        cnt += (total_time//t)
    return cnt
        

def solution(n, times):
    r,l = sys.maxsize,0
    res = sys.maxsize
    while l<=r:
        mid = (l+r)//2
        if getThroughput(mid, times) >= n:
            res = mid
            r = mid-1
        else:
            l = mid+1    
    
    return res