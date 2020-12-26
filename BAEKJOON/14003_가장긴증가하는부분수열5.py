import sys
read=sys.stdin.readline

def bin_search(i):
    x = num[i]
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
    num_index[i] = tmp

n = int(read())
num = list(map(int,read().split()))
num_index = list(0 for _ in range(n))
dp = [num[0]]
for i in range(1,n):
    if num[i] > dp[-1]:
        dp.append(num[i])
        num_index[i] = len(dp)-1
    elif num[i] < dp[-1]:
        bin_search(i)

len_dp = len(dp) 
answer = []
tmp = len_dp-1
for i in range(n-1, -1, -1):
    if num_index[i] == tmp:
        tmp-=1
        if len_dp == -1: break
        answer.append(num[i])
        
print(len_dp)
print(*answer[::-1])