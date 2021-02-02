import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def solution(a):
    import sys
    import heapq as hq
    answer = 1
    n=len(a)

    right = a[1::]
    hq.heapify(right)
    left = set()
    left_min = sys.maxsize
    
    for i in range(n-1):
        #check
        if a[i] < left_min or a[i] < right[0]:
            answer += 1
        #left
        if a[i] < left_min:
            left_min = a[i]
        left.add(a[i])
        #right
        if right[0] == a[i+1]:
            hq.heappop(right)
            while right and right[0] in left:
                hq.heappop(right)

    return answer

a = [9,-1,-5]
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))