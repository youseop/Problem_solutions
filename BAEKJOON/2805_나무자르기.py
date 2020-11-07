import sys
read = sys.stdin.readline
n, tree = map(int, read().split())
num = list(map(int, read().split()))
r, l = max(num), 0


def TREE(x):
    sum_tree = 0
    for i in num:
        if i > x:
            sum_tree += (i-x)
    return sum_tree


while l <= r:
    mid = (l+r)//2
    sum_tree = TREE(mid)

    if sum_tree >= tree:
        l = mid+1
        answer = mid
    else:
        r = mid-1

print(answer)
