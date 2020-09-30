import sys
import heapq
n = int(input())
numbers = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if numbers:
            if numbers[0][1] == 1:
                print(heapq.heappop(numbers)[0])
            else:
                print(-heapq.heappop(numbers)[0])
        else:
            print(0)
    else:
        if num > 0:
            heapq.heappush(numbers, (num, 1))
        else:
            heapq.heappush(numbers, (-num, 0))
