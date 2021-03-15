import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def SizeToCount(size):
    buffer = 0
    cnt = 0
    for b in blue:
        if b > size:
            return sys.maxsize
        if buffer + b > size:
            cnt += 1
            buffer = b
        else:
            buffer += b
    if buffer > 0: cnt += 1
    return cnt
        

n,m = map(int,read().split())
blue = list(map(int,read().split()))

l,r = 1,sum(blue)
while l<=r:
    mid = (l+r)//2
    if SizeToCount(mid) > m:
        l = mid + 1
    elif SizeToCount(mid) <= m:
        save = mid
        r = mid - 1

print(save)
