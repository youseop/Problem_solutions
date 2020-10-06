import sys

n = int(input())
numbs = list(map(int, input().split()))

save = 0  # 내림차순이 시작되는 위치 저장
for i in range(n-1, -1, -1):
    if numbs[i] > numbs[i-1]:
        save = i
        break
    if i-1 == 0:
        save = 0
        break

if save == 0:
    print(-1)
    sys.exit()
#    수열 전체가 내림차순이면 다음 순열이 없음으로
#    -1 출력 후 시스템종료

front = numbs[save-1]
Descending = numbs[save:]

tmp = Descending+[front]
tmp.sort()
index_front = tmp.index(front)
new_front = tmp[index_front+1]

tmp.remove(new_front)
tmp.sort()

answer = numbs[:save-1]+[new_front]+tmp
print(*answer)
