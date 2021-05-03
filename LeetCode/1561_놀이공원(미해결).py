import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline


def getChildNum(T,times):
    totChildren = len(times)
    ridesList = []
    for index,time in enumerate(times):
        totChildren += T//time
        if T%time == 0:
            ridesList.append(index+1)
    return totChildren,ridesList


n,m = map(int,read().split())
times = list(map(int,read().split()))

l,r = 0, sys.maxsize
while l<=r:
    mid = (l+r)//2
    totChildren, ridesList = getChildNum(mid,times)
    if totChildren == n:
        break
    elif totChildren < n:
        l = mid+1
    else:
        r = mid-1
        
offset = totChildren - n
print(ridesList[-(offset+1)])