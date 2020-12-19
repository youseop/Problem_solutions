import sys
read=sys.stdin.readline

def largest():
    answer = 0
    
    for height in list(set(rect)):
        cnt = 0
        for h in rect:
            if h >= height:
                cnt += 1
            else:
                answer = max(answer, cnt * height)
                cnt = 0
    answer = max(answer, cnt * height)
    return answer

while 1:
    n,*rect = list(map(int,read().split()))
    if n == 0: break
    print(largest())