from math import ceil

def getnum(i,arr):
    arr = list(arr)
    return arr[i]

def solution(n, k):
    answer = []
    dp = list(1 for _ in range(n))
    for i in range(2, n):
        dp[i] = dp[i-1]*i
    nums = set(i for i in range(1,n+1))
    for i in range(n-1,-1,-1):
        a = ceil(k/dp[i])
        tmp = getnum(a-1, nums)
        answer.append(tmp)
        nums.remove(tmp)
        k -= (dp[i]*(a-1))
    return answer