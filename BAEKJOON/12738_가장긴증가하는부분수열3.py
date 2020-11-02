import sys
sys.stdin = open("input.txt", "rt")
read = sys.stdin.readline

n = int(read())
num = list(map(int, read().split()))

dp = [num[0]]


def binsearch(x):
    l, r = 0, len(dp)
    while True:
        mid = (l+r)//2
        if dp[mid] == x:
            break
        elif mid == 0:
            if dp[mid] > x:
                dp[mid] = x
                break
            else:
                l += 1
        elif dp[mid] > x:
            if dp[mid-1] < x:
                dp[mid] = x
                break
            elif dp[mid-1] == x:
                break
            else:
                r = mid-1
        else:
            l = mid+1
    return


for x in num[1:]:
    if x > dp[-1]:
        dp.append(x)
    else:
        if len(dp) != 1:
            binsearch(x)
        else:
            dp = [x]
print(len(dp))
