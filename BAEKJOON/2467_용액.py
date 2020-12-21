##########################이분탐색##################################
import sys
read=sys.stdin.readline

def bin_search(i):
    global answer
    x = liqs[i]
    l = i + 1 #index == i인 수와 index > i인 수들을 비교한다.
    r = n - 1
    while l <= r:
        mid = (l+r)//2
        diff = liqs[mid] + x
        if diff < 0:    #0보다 작으면 더 큰 수와 더해본다.
            l = mid + 1 
        elif diff > 0:  #0보다 크면 더 작은 수와 더해본다.
            r = mid - 1
        else:           #0이면 두 수를 출력하고 종료
            print(x, liqs[mid])
            sys.exit()
        #합이 0에 더 가까우면 answer 갱신
        if abs(diff) < answer[0]:
            answer = [abs(diff), [x, liqs[mid]]]

n = int(read())
liqs = sorted(map(int,read().split()))
answer = [sys.maxsize,[-1,-1]]

for i in range(n):
    bin_search(i)

print(*answer[1])