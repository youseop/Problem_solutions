import sys
from collections import deque
read=sys.stdin.readline

n,k=map(int,read().split())
#해당 좌표까지 이동하는데 걸리는 시간 저장
dp=list(-1 for _ in range(max(n,k)*2+1))
dp[n]=0
#해당 좌표로 오기 이전의 좌표 저장(경로 확인 용도)
path=list(0 for _ in range(max(n,k)*2+1))
path[n]=-1
#BFS
point=deque([n])
while point:
    a=point.popleft()
    #동생을 찾은 경우 시간과 경로를 출력하고 시스템을 종료한다.
    if a==k:
        print(dp[a])
        way=[]
        #경로 복원
        while True:
            way.append(a)
            a=path[a]
            if a == -1:
                print(*way[::-1])
                break
        sys.exit()
    else:
        if a-1>=0 and dp[a-1]==-1:
            dp[a-1]=dp[a]+1
            path[a-1]=a
            point.append(a-1)
        if a+1<=k*2 and dp[a+1]==-1:
            dp[a+1]=dp[a]+1
            path[a+1]=a
            point.append(a+1)
        if a*2<=k*2 and dp[a*2]==-1:
            dp[a*2]=dp[a]+1
            path[a*2]=a
            point.append(a*2)


