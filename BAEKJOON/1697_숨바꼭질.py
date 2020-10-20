from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
# n-수빈 k-동생
bfs = deque([n])
maxnk = max(n, k)
dp = list(-1 for _ in range(2*maxnk+1))
dp[n] = 0


def BFS():
    while bfs:
        p = bfs.popleft()
        p1 = p*2
        p2 = p+1
        p3 = p-1
        for x in [p1, p2, p3]:
            if 0 <= x < 2*(maxnk)+1 and dp[x] == -1:
                dp[x] = dp[p]+1
                if x == k:
                    print(dp[x])
                    sys.exit()
                bfs.append(x)


if n == k:
    print(0)
else:
    BFS()
    print('error')
