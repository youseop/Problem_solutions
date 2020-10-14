import sys
read = sys.stdin.readline

n = int(read())
numbs = list(map(int, read().split()))

dp = list(list(0 for _ in range(n)) for _ in range(n))
for i in range(n):
    dp[i][i] = 1
    if i+1 < n:
        dp[i+1][i] = 1

for k in range(1, n):
    for i in range(n-k):
        x = i
        y = i+k
        if dp[x+1][y-1] != 0 and numbs[x] == numbs[y]:
            dp[x][y] = 1

for _ in range(int(read())):
    a, b = map(int, read().split())
    if dp[a-1][b-1] == 0:
        print(0)
    else:
        print(1)
