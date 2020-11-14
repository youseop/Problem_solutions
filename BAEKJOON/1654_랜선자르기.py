import sys
read = sys.stdin.readline

k, n = map(int, read().split())

LAN = list(int(read()) for _ in range(k))

MAX_LAN = sum(LAN)//n
if MAX_LAN == 1:
    print(1)
    sys.exit()
MIN_LAN = 0


def cut(x):
    tot = 0
    for l in LAN:
        tot += l//x
    return tot


answer = 0
while MAX_LAN >= MIN_LAN:
    mid = (MIN_LAN+MAX_LAN)//2
    if cut(mid) >= n:
        answer = max(answer, mid)
        if answer == mid:
            MIN_LAN = mid+1
        else:
            break
    else:
        MAX_LAN = mid-1
print(answer)
