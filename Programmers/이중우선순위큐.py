import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

from heapq import heapify,heappush,heappop

def solution(operations):
    key = 0
    removed = set()
    maxH = []
    minH = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heappush(minH,(num,key))
            heappush(maxH,(-num,key))
            key += 1
        elif num == -1:#최소값 삭제
            while minH and minH[0][1] in removed:
                heappop(minH)
            if minH:
                removed.add(heappop(minH)[1])
        else:#최댓값 삭제
            while maxH and maxH[0][1] in removed:
                heappop(maxH)
            if maxH:
                removed.add(heappop(maxH)[1])
        print
    while minH and minH[0][1] in removed:
        heappop(minH)
    while maxH and maxH[0][1] in removed:
        heappop(maxH)

    if minH:
        return [-maxH[0][0],minH[0][0]]
    return [0,0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

