import sys


def possible(x, y):
    # 1-9까지의 숫자중 어떤 숫자가 비어있는지 확인
    numlist = list(range(1, 10))
    # 1-9로 이루어진 리스트 numlist를 생성하고,
    # 가로, 세로, 상자내에 존재하는 숫자들을 제거해 나간다.
    for i in range(9):
        # 가로
        if numbs[x][i] in numlist:
            numlist.remove(numbs[x][i])
        # 세로
        # 여기서 elif로 쓰는 실수를 해서 1시간 동안 고민했었는데 반드시 if 문을 써주어야한다!
        if numbs[i][y] in numlist:
            numlist.remove(numbs[i][y])
    # 상자
    a = (x//3)*3
    b = (y//3)*3
    for i in range(3):
        for j in range(3):
            if numbs[a+i][b+j] in numlist:
                numlist.remove(numbs[a+i][b+j])

    return numlist  # 빈칸에 들어갈 수 있는 숫자들 return

# 정답이 여러개라면 아무거나 출력해도 상관 없음으로
# 0인 칸에 들어갈 수 있는 수들에 대해서 dfs진행


def dfs(x):
    if x == len(zero):
        for i in numbs:
            print(*i)
        sys.exit()  # 스도쿠가 출력되었으면 시스템 종료!

    a = zero[x][0]
    b = zero[x][1]
    N = possible(a, b)

    for n in N:
        numbs[a][b] = n
        dfs(x+1)
        numbs[a][b] = 0
    return


numbs = list(list(map(int, sys.stdin.readline().split())) for _ in range(9))
# 0인 칸들의 좌표들을 zero에 추가
zero = []
for i in range(9):
    for j in range(9):
        if numbs[i][j] == 0:
            zero.append([i, j])

dfs(0)
