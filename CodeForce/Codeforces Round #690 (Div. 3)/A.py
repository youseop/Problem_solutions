import sys, math
read=sys.stdin.readline
from collections import deque

N = int(read())
for _ in range(N):
    n = int(read())
    num = deque(list(map(int,read().split())))
    answer = []
    left = True
    for i in range(n):
        if left:
            answer.append(num.popleft())
            left = False
        else:
            answer.append(num.pop())
            left = True

    print(*answer)
