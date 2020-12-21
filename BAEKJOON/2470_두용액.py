######################투 포인터#######################
import sys
read=sys.stdin.readline

n=int(read())
liq = sorted(map(int,read().split()))
l=0
r=n-1

answer = [sys.maxsize, -1, -1]
while l < r:
    diff = liq[r] + liq[l]
    abs_diff = abs(diff)

    if answer[0] > abs_diff:
        answer = [abs_diff, liq[l], liq[r]]

    if diff == 0: 
        break
    elif diff > 0:
        r -= 1
    else:
        l += 1
        
print(*answer[1:])

######################절대값 기준 정렬#######################
import sys
read=sys.stdin.readline

n = int(read())
liq = sorted(map(int,read().split()), key = lambda x : abs(x))

answer = sys.maxsize
two_liq = [0,0]

for i in range(1,n):
    tmp = abs(liq[i]+liq[i-1])
    if answer > tmp:
        answer = tmp
        two_liq = [liq[i-1],liq[i]]

print(*sorted(two_liq))

