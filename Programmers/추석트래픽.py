
def solution(lines):
    import heapq as hq
    answer = 0
    n= len(lines)
    time = []
    for i in range(n-1,-1,-1):
        lines[i] = list(lines[i].split())[1:]
        x,y,z = lines[i][0].split(":")
        end_time = int(float(z)*1000 + int(y)*60000 + int(x)*3600000)
        start_time = int(end_time - float(lines[i][1][:-1])*1000 + 1)
        time.append((start_time,end_time))

    heap = []
    for t in time:
        
        hq.heappush(heap,-t[0])
        while -heap[0] >= t[1] + 1000:
            hq.heappop(heap)
        answer = max(answer , len(heap))

    return answer
