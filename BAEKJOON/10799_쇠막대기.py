import sys
read=sys.stdin.readline
from collections import deque

sticks = list(read().strip())
sticks = deque(sticks)

stack = []

cnt = -1
res = 0

while sticks:
    if sticks[0] == '(':
        laser = True
        cnt += 1
        stack.append(sticks.popleft())
    elif sticks[0] == ')':
        if laser:
            res += cnt
            laser = False
        else:
            res += 1
        stack.pop()
        sticks.popleft()
        cnt -= 1
print(res)

