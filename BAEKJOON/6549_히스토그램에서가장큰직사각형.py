import sys
read=sys.stdin.readline

def maxSize():
    max_size = 0 #최대 넓이 저장
    stack = []

    for i in range(N):
        #왼쪽으로 이어질 수 있는 index
        min_point = i
        while stack and stack[-1][0] >= rect[i]:
            #pop되었다는 것은 추가 될 직사각형보다 높이가 높다는 의미이다.
            #따라서 추가될 직사각형은 pop되는 직사각형의 point값까지 넓어질 수 있다!
            #pop된 사각형의 point값으로 min_point를 업데이트
            h, min_point = stack.pop()
            tmp_size = h * (i-min_point)
            max_size = max(max_size, tmp_size)
        stack.append([rect[i],min_point])
    #탐색이 끝나고 아직 Stack에 남은 직사각형 정보로 maxSize 갱신
    for h, point in stack:
        max_size = max(max_size, (N-point)*h)

    return max_size

while True:
    N, *rect = map(int,read().split())
    if N == 0: 
        break
    print(maxSize())