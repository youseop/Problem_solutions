import sys
read = sys.stdin.readline

N = int(read())
num = list(map(int, read().split()))

dp = [num[0]]


def bin_search(x):
    a = 0
    b = len(dp)-1
    while a <= b:
        mid = (a+b)//2
        if dp[mid] > x:
            if 0 <= mid-1 and dp[mid-1] < x:
                dp[mid] = x
                break
            elif dp[0] > x:
                dp[0] = x
                break
            else:
                b = mid-1
        else:
            a = mid+1


for n in num[1:]:
    if n > dp[-1]:
        dp.append(n)
    else:
        bin_search(n)

print(N-len(dp))
