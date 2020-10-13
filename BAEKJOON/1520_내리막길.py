import sys
sys.stdin = open("input.txt", "rt")

read = sys.stdin.readline
sys.setrecursionlimit(1000000000)  # 중요!
m, n = map(int, read().split())
stairs = list(list(map(int, read().split())) for _ in range(m))

dp = list(list(-1 for _ in range(n)) for _ in range(m))
dp[-1][-1] = 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for x, y in zip(dx, dy):
        if 0 <= i+x < m and 0 <= j+y < n and stairs[i+x][j+y] < stairs[i][j]:
            dp[i][j] += dfs(i+x, j+y)
    # for x in dp:
    #     print(*x)
    # print()
    return dp[i][j]


print(dfs(0, 0))


# 시행착오!!
'''
import sys
read=sys.stdin.readline

m,n=map(int,read().split())
stairs=list(list(map(int,read().split())) for _ in range(m))

dp=list(list(0 for _ in range(n)) for _ in range(m))

for i in range(n):
    dp[0][i]=1

for i in range(1,m):
    save=list(0 for _ in range(n))
    for j in range(n):
        if stairs[i][j]<stairs[i-1][j]: 
            save[j]=dp[i-1][j]
            dp[i][j]=dp[i-1][j]
    for j in range(n):
        x,y=j,j
        while True:
            if x<=0 or stairs[i][x]>=stairs[i][x-1]: break
            dp[i][j]+=save[x-1]
            x-=1
        while True:
            if y+1>=n or stairs[i][y]>=stairs[i][y+1]: break
            dp[i][j]+=save[y+1]
            y+=1
        #print('save:',save)

print(dp[-1][-1])'''
