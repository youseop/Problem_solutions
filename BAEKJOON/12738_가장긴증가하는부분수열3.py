import sys
read=sys.stdin.readline

def bin_search(x):
    l, r = 0, len(dp)-1
    while l<=r:
        mid = (l+r)//2
        if dp[mid] == x:
            return
        elif dp[mid] > x:
            tmp = mid
            r = mid - 1
        else:
            l = mid + 1
    dp[tmp] = x

n = int(read())
num = list(map(int,read().split()))
dp = [num[0]]
for i in range(1,n):
    if num[i] > dp[-1]:
        dp.append(num[i])
    elif num[i] < dp[-1]:
        bin_search(num[i])
print(len(dp))