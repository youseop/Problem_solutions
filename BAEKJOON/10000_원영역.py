import sys
read=sys.stdin.readline
from collections import deque

get_input = []
n = int(read()) 

for _ in range(n):
    a,b = map(int,read().split())
    get_input.append((a-b, 1, -b*2))
    get_input.append((a+b, 0, b*2))

get_input.sort(key = lambda x : (x[0], x[1], x[2]))
get_input = deque(get_input)

cnt = 1 + n
stack = []
while get_input:
    tmp = get_input.popleft()
    if tmp[1]:
        stack.append([tmp[0],tmp[1],abs(tmp[2]),abs(tmp[2])])
    else:
        circle = stack.pop()
        if circle[3] == 0:
            cnt+=1
        if stack:
            stack[-1][3] -= circle[2]
print(cnt)
        