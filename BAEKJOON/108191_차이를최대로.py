import sys
read=sys.stdin.readline

from collections import deque

n=int(read())
num=sorted(list(map(int,read().split())))

save=deque()

for i in range(n//2):
    if i%2 ==0:
        save.append(num[i])
        save.appendleft(num[n-1-i])
    else:
        save.appendleft(num[i])
        save.append(num[n-1-i])

if n%2 ==1:
    if abs(save[0] - num[n//2]) > abs(save[-1] - num[n//2]):
        save.appendleft(num[n//2])
    else:
        save.append(num[n//2])
answer=0
for i in range(1,n):
    answer+=abs(save[i-1]-save[i])
print(answer)
