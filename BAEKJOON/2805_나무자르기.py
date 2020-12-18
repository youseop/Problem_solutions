import sys
sys.stdin = open('text.txt','rt')
read=sys.stdin.readline

n,m=map(int,read().split())
wood = list(map(int,read().split()))

low = 0
high = int(10e9 +1)

while low+1<high:
    print(low, high)
    mid = (low+high)//2
    get_wood = 0
    for w in wood:
        get_wood += max(0, w - mid)

    if get_wood >= m:
        low = mid
    else:
        high = mid

print(low)
############################

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
