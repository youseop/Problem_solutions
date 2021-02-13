import math

def solution(n, stations, w):
    answer = 0
    stacks = [0]
    for station in stations:
        if station-w < 1:
            stacks.append(1)
            stacks.append(station+w)
        elif stacks and station-w <= stacks[-1]:
            stacks[-1] = station+w
        else:
            stacks.append(station-w)
            stacks.append(station+w)
            
    if stacks[-1] < n:
        stacks.append(n+1)
    else:
        stacks.pop()
        
    for i in range(0,len(stacks),2):
        answer += math.ceil((stacks[i+1]-stacks[i]-1)/(2*w+1))

    return answer