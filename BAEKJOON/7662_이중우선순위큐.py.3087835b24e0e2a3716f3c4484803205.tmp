import sys
import heapq

for _ in range(int(input())):
    k=int(input())
    ids=list(sys.stdin.readline().split() for _ in range(k))
    for i in range(len(ids)):
        ids[i][1]=int(ids[i][1])

    min_hq=[]
    max_hq=[]
    key=[False]*1000001

    for index,id in enumerate(ids):
        if id[0]=='I': 
            heapq.heappush( min_hq, (id[1],index))
            heapq.heappush( max_hq, (-id[1],index))
            key[index]=True

        elif id[1]==-1:
            while min_hq and not key[min_hq[0][1]]:
                heapq.heappop(min_hq)
            if min_hq:
                key[heapq.heappop(min_hq)[1]]=False
                

        elif id[1]==1:
            while max_hq and not key[max_hq[0][1]]:
                heapq.heappop(max_hq)
            if max_hq:
                key[heapq.heappop(max_hq)[1]]=False
                

    while min_hq:
        if not key[min_hq[0][1]]:
            heapq.heappop(min_hq)
        else: break

    while max_hq:
        if not key[max_hq[0][1]]:
            heapq.heappop(max_hq)
        else: break

    if not min_hq or not max_hq: print('EMPTY')
    else:
        print(-heapq.heappop(max_hq)[0], heapq.heappop(min_hq)[0])


