from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
map = list(list(map(int, read().split())) for _ in range(n))

for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            # 아기상어가 있는 위치를 입력하고, 해당 위치를 0으로 초기화
            A, B = i, j
            map[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs():
    shark_shape = 2  # 최초의 상어 크기는 2다.
    shark_exp = 0  # 상어가 몸집이 커지기위한 경험치라고 생각하면 된다.
    point = deque([[A, B]])

    answer = 0
    flag = False
    # 상어가 물고기를 먹었을 때, 첫 번째 for문을 한번만 돌고 탈출할 수 있도록 한다.
    visited = list(list(-1 for _ in range(n)) for _ in range(n))
    visited[A][B] = 0
    # BFS를 진행하며 상어가 방문했는지, 방문했다면 해당 점까지의 거리가 몇인지 저장

    while point:
        # 자신보다 큰 물고기들에 갇혔다면, 원소들이 지속적으로 point에
        # 추가되지 않아, while문이 종료된다.

        term = len(point)
        point = deque(sorted(point))
        # 위, 왼쪽에 위치한 먹이들을 우선적으로 먹기 위해 정렬

        for _ in range(term):
            a, b = point.popleft()

            if 0 < map[a][b] < shark_shape:
                map[a][b] = 0
                shark_exp += 1
                if shark_exp == shark_shape:
                    # 경험치가 상어의 몸집만큼 쌓였다면, 레벨업 시키고
                    # 경험치를 다시 0으로 초기화
                    shark_exp = 0
                    shark_shape += 1
                point = deque()
                answer += visited[a][b]  # 해당 점까지의 거리를 더해준다.
                # 물고기를 먹은 자리에서 다시 거리를 계산해 나가야 함으로 visited리스트 초기화
                visited = list(list(-1 for _ in range(n)) for _ in range(n))
                visited[a][b] = 0
                flag = True

            for x, y in zip(dx, dy):
                ax, by = a+x, b+y
                if 0 <= ax < n and 0 <= by < n and visited[ax][by] == -1 and map[ax][by] <= shark_shape:
                    visited[ax][by] = visited[a][b]+1
                    point.append([ax, by])
            if flag:
                flag = False
                break
    return answer


answer = bfs()
print(answer)
