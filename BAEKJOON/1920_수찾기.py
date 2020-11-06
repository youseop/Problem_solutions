import sys
read = sys.stdin.readline

n = int(read())
A = list(map(int, read().split()))
A.sort()
m = int(read())
num = list(map(int, read().split()))


def binsearch(x):
    if x > A[-1] or x < A[0]:
        return 0
    if x == A[-1] or x == A[0]:
        return 1
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if A[mid] == x:
            return 1
        elif A[mid] < x:
            l = mid+1
        else:
            r = mid-1
    return 0

    # 이렇게 while문 다 돌고 나서도 x를 찾지 못한 경우에
    # 0을 return해줘야 하는데 이걸 생각못했었다.
for i in num:
    print(binsearch(i))
