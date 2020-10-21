import sys
read = sys.stdin.readline

r, c, t = map(int, read().split())
dust = list(list(map(int, read().split())) for _ in range(r))

d = []  # 공기청정기 위치 확인
for i in range(r):
    if dust[i][0] == -1:
        d.append(i)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def diffusion():
    add = list(list(0 for _ in range(c)) for _ in range(r))
    # 바로바로 더해주면서 가면 다음 칸에서 누적이 발생함으로 리스트 두개로 운영
    for i in range(r):
        for j in range(c):

            if dust[i][j] > 0:
                cnt = 0  # 몇개방향으로 확산되는지 확인
                for x, y in zip(dx, dy):
                    ix, jy = i+x, j+y
                    if 0 <= ix < r and 0 <= jy < c and dust[ix][jy] != -1:
                        add[ix][jy] += dust[i][j]//5
                        cnt += 1
                dust[i][j] -= (dust[i][j]//5)*cnt
    for i in range(r):
        for j in range(c):
            dust[i][j] += add[i][j]
    return


def cycle():
    # 1
    for i in range(d[0]-1, 0, -1):
        dust[i][0] = dust[i-1][0]
    for i in range(d[1]+1, r-1):
        dust[i][0] = dust[i+1][0]
    # 2
    for i in range(c-1):
        dust[0][i] = dust[0][i+1]
        dust[-1][i] = dust[-1][i+1]
    # 3
    for i in range(d[0]):
        dust[i][-1] = dust[i+1][-1]
    for i in range(r-1, d[1], -1):
        dust[i][-1] = dust[i-1][-1]
    # 4
    for i in range(c-1, 1, -1):
        dust[d[0]][i] = dust[d[0]][i-1]
        dust[d[1]][i] = dust[d[1]][i-1]
    dust[d[0]][1] = 0
    dust[d[1]][1] = 0
    return


for _ in range(t):
    diffusion()
    cycle()

sum_dust = 2  # 공기청정기의 -1이 두개 있음으로 2를 더해주고 시작
for D in dust:
    sum_dust += sum(D)

print(sum_dust)
