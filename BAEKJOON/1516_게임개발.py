from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
# 해당 점이 선행되어야 하는 점들 저장
before = list([] for _ in range(n+1))
# 선행되어야 하는 점의 개수가 몇개 남았는지 저장
left_num = [0]
# 해당 건물(점)을 짓는데 걸리는 시간 저장
time = list(0 for _ in range(n+1))

point = deque([])
for i in range(1, 1+n):
    tmp = list(map(int, read().split()))
    time[i] = tmp[0]  # 건물 짓는데 걸리는 시간 저장
    for j in tmp[1:-1]:
        before[j].append(i)
    left_num.append(len(tmp[1:-1]))
    if tmp[1:-1] == []:
        point.append([i, time[i]])
# 출력하기 위한 값들 저장
answer = list(0 for _ in range(n+1))
# 해당 건물을 짓기전 선행되어야 하는 건물들을 짓는데 걸리는 시간 저장
rest = list(0 for _ in range(n+1))

while point:
    a, w = point.popleft()
    answer[a] = w
    for i in before[a]:
        if left_num[i] != 0:
            left_num[i] -= 1
            rest[i] = max(rest[i], w)
            if left_num[i] == 0:
                point.append([i, rest[i]+time[i]])
for i in answer[1:]:
    print(i)
