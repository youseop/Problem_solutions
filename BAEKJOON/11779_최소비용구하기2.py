import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

n=int(read())
m=int(read())

bridge=dict()
for _ in range(m):
    a,b,c=map(int,read().split())
    a,b=a-1,b-1
    if a not in bridge:
        bridge[a]=[]
    bridge[a].append((b,c))

start,end=map(int,read().split())
start,end=start-1,end-1
#이전 노드 저장
way=list(-1 for _ in range(n))
#start로부터 최단거리 저장
dp=list(inf for _ in range(n))
dp[start]=0

point=[[0, start]]
#heapq를 사용해 아직 방문하지 않은 점들 중 최단거리의 점 탐색
hq.heapify(point)

while point:
    w_a, a = hq.heappop(point)
    if a == end:
        print(dp[a])
        break
    if a in bridge:
        for x, w_x in bridge[a]:
            if dp[x] > w_a + w_x:
                #x의 최단거리 업데이트
                dp[x] = w_a + w_x
                #이전 노드 저장
                way[x] = a
                #heapq에 노드 추가
                hq.heappush(point,[dp[x], x])

#경로 복원
memo_way=[]
while True:
    memo_way.append(a+1)
    a=way[a]
    if a ==-1:
        break

print(len(memo_way))
print(*memo_way[::-1])