import sys
read=sys.stdin.readline

n = int(read())
dist = list(map(int,read().split()))
price = list(map(int,read().split()))[:-1]

answer = price[0]*dist[0]
tmp = price[0]
for i in range(1,n-1):
    if tmp > price[i]:
        tmp = price[i]
    answer += tmp * dist[i]

print(answer)
