import sys
from collections import deque
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

n,k = map(int,read().split())
num = list(i for i in set(int(read()) for _ in range(n))if i <=k)
n = len(num)
point = deque([(i,num[i]) for i in range(n)])
visit = list(1 for _ in range(k+1))
for i in num:
    visit[i] = 0

cnt = 1
while point:
    for _ in range(len(point)):
        index, sum_num = point.popleft()
        for i in range(index, n):
            next_num = sum_num+num[i] 
            if sum_num == k:
                print(cnt)
                exit()
            elif next_num <= k and visit[next_num]:
                point.append((i,next_num))
                visit[next_num] = 0
    cnt += 1
print(-1)
