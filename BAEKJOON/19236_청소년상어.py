import sys
read=sys.stdin.readline
sys.setrecursionlimit(100000)
D = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

def fish_move(fish_index, MAP):
    for i in range(1,17):
        a,b = fish_index[i]
        if a == -1 and b == -1: continue
        fish_d = MAP[a][b][1]
        #print(a,b,fish_d)
        while True:
            ax, by = D[fish_d][0]+a, D[fish_d][1]+b
            if 0<=ax<4 and 0<=by<4 and MAP[ax][by][0] != -1:
                fish_change = MAP[ax][by][0]
                MAP[a][b] = MAP[ax][by][:]
                MAP[ax][by] = [i,fish_d]
                fish_index[fish_change] = [a,b]
                fish_index[i] = [ax,by]
                break
            fish_d += 1
            if fish_d == 8:
                fish_d = 0
    return

def dfs(shark_exp, shark_p, shark_direction, arr, index):
    global answer
    MAP = list(list([] for _ in range(4)) for _ in range(4))
    fish_index = index[::]
    for i in range(4):
        for j in range(4):
            MAP[i][j] = arr[i][j][::]
    fish_move(fish_index, MAP)

    dx,dy = D[shark_direction]
    a,b = shark_p
    flag = True
    for i in range(1,4):
        ax, by = a+dx*i, b+dy*i
        if 0<=ax<4 and 0<=by<4:
            if MAP[ax][by][0] > 0:
                tmp1,tmp2 = fish_index[MAP[ax][by][0]]
                tmp3 = MAP[ax][by][0]

                fish_index[MAP[ax][by][0]] = [-1,-1]
                MAP[ax][by][0] = -1
                MAP[a][b][0] = 0
                ################################################################
                dfs(shark_exp + tmp3, [ax,by], MAP[ax][by][1], MAP, fish_index)
                ################################################################
                MAP[ax][by][0] = tmp3
                fish_index[MAP[ax][by][0]] = [tmp1,tmp2]
                MAP[a][b][0] = -1
                flag = False
        else:
            break
    if flag:
        answer = max(answer, shark_exp)
    return

shark_exp = 0
MAP = [[],[],[],[]] #지도
fish_index = list([] for _ in range(17)) #물고기 위치

for j in range(4):
    tmp = list(map(int,read().split()))
    for i in range(4):
        fish_index[tmp[i*2]] = [j,i] 
        MAP[j].append([tmp[i*2],tmp[i*2+1]-1])

shark_p = [0,0]
shark_direction = MAP[0][0][1] #상어 방향 업데이트
shark_exp += MAP[0][0][0] #물고기 크기만큼 경험치 반영
answer = shark_exp
#상어가 먹은 물고기의 fish_index [-1,-1]로 변경
fish_index[MAP[0][0][0]] = [-1,-1] 
#상어 자리 -1로 변경
MAP[0][0][0] = -1 

dfs(shark_exp, shark_p, shark_direction, MAP, fish_index)
print(answer)