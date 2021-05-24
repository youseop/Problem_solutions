import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline

from collections import deque

def bfs(v):
    count=0
    q=deque([v])
    while q:
        print(q)
        v = q.popleft() #count는 큐에 달고다니면서 계산하는거보다 while문 돌때마다 증가시키는게 공간복잡도적으로도 효율적이고 읽는사람이 직관적으로 받아들일듯
        #여기 등록되는 점들은 다 visited False처리가 이미 된 점들이니까 굳이 if문 사용 안해도 될듯
        for e in adj[v]:
            if not visited[e]:
                visited[e] = True #큐에 집어넣을때 visited처리해서 넣자
                q.append(e)
        count +=1


    return count-1 #시작점은 제외하고 count해야함으로

   


n= int(input())
m= int(input())
adj=[[]for _ in range(n+1)]
visited=[False]*(n+1)
visited[1] = True #미리 시작점은 True처리하고 시작해야 좋을듯

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs(1))