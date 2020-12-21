import sys
read=sys.stdin.readline

def bin_search(x, w):
    l,r = 0, M -1
    while l <= r:
        mid = (l+r)//2
        x_s = shoot[mid]
        if x_s >= x-w and x_s <= x+w: return 1
        elif x_s < x-w: l = mid + 1
        else: r = mid - 1
    return 0

M, N, L = map(int,read().split())
shoot = sorted(map(int,read().split()))
animal = list(x for x in list(list(map(int,read().split())) 
                              for _ in range(N)) if x[1] <= L)
cnt = 0
for x, y in animal:
    cnt += bin_search(x, abs(L-y))

print(cnt)

