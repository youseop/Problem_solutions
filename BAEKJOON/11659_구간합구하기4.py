import sys
read=sys.stdin.readline

n,m = map(int,read().split())
num = [0]+list(map(int,read().split()))
for i in range(n):
    num[i+1] += num[i]


for _ in range(m):
    a,b = map(int,read().split())
    print(num[b] - num[a-1])