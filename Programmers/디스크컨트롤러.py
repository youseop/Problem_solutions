
from heapq import heapify, heappush, heappop

def duration(x):
    return x[1]-x[0]

def solution(jobs):
    n = len(jobs)
    end_time = -1
    jobs.sort(reverse = True)
    waiting = []
    end_time = 0
    tot_time = 0
    while jobs or waiting:
        while jobs and jobs[-1][0]<=end_time:
            s,t = jobs.pop()
            heappush(waiting,(t,s))

        if waiting:
            t,s = heappop(waiting)
            end_time += t
            tot_time += (end_time - s)
        else:
            s,t = jobs.pop()
            end_time = s+t
            tot_time += t

    return tot_time//n