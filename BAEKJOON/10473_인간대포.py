import sys
import heapq as hq
read=sys.stdin.readline
inf = sys.maxsize

def dist(start,end):
    return sum((i-j)**2 for i,j in zip(start, end))**(1/2)

start = list(map(float,read().split()))
end = list(map(float,read().split()))
m = int(read())
fort = list(list(map(float,read().split())) for _ in range(m))
bridge = list(list(0 for _ in range(m+2)) for _ in range(m+2))

#출발지점부터 도착지까지의 시간
bridge[0][m+1] = round(dist(start,end)/5,4)

#출발지점부터 각 대포까지의 시간
for i in range(m):
    bridge[0][i+1] = round(dist(start, fort[i])/5,4)
    
#대포간에 걸리는 시간
for i in range(m):
    for j in range(i+1,m):
        bridge[i+1][j+1] = round(abs(50-dist(fort[i],fort[j]))/5+2,4)
        bridge[j+1][i+1] = bridge[i+1][j+1]
        
#대포로 부터 도착지까지의 시간
for i in range(m):
    bridge[i+1][-1] = round(abs(50-dist(fort[i],end))/5+2,4)
    
#다익스트라
def Dijkstra():
    point = [(0, 0)]
    visit = list(inf for _ in range(m+2))
    visit[0] = 0
    while point:
        dist, node = hq.heappop(point)
        if node == m+1:
            print(dist)
            break
        for i in range(1,m+2):
            if visit[i] > dist + bridge[node][i]:
                visit[i] = dist + bridge[node][i]
                hq.heappush(point,(visit[i], i))


Dijkstra()