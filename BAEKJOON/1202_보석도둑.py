import sys
from heapq import heappop, heapify, heappush
read=sys.stdin.readline


def main():
    n,k = map(int,read().split())
    jew = list(list(map(int,read().split())) for _ in range(n))
    heapify(jew)
    knapsacks = sorted(int(read()) for _ in range(k))

    cand = [] #현재 knapsack에 들어갈 수 있는 보석들의 후보
    total = 0 #보석 무게 총합
    for knapsack in knapsacks:
        while jew and jew[0][0] <= knapsack:
            heappush(cand,-heappop(jew)[1])
        if cand:
            total -= heappop(cand)

    print(total)
    
if __name__ == '__main__':
    main()