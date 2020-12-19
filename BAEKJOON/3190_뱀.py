import sys
sys.stdin = open('text.txt','rt')
read=sys.stdin.readline
from collections import deque

def check_dir(time,direction):
    if command[time]:
        if command[time] == 'D': #right
            direction += 1
            if direction >= 4: direction = 0
        else:                    #left
            direction -= 1
            if direction < 0: direction = 3
    return direction

def check_way():
    if any(0>i or n<=i for i in N_P) or check[N_P[0]][N_P[1]] == 0:
        return False

    elif check[N_P[0]][N_P[1]] == '*':
        check[N_P[0]][N_P[1]] = 0
        snake.append([N_P[0],N_P[1]])

    else:
        check[N_P[0]][N_P[1]] = 0
        snake.append([N_P[0],N_P[1]])
        a,b=snake.popleft()
        check[a][b] = 1
    return True

dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = 0 #0,1,2,3 - 우,하,좌,상
snake = deque([[0,0]])
time=0

n=int(read())
check = list(list(1 for _ in range(n)) for _ in range(n))
check[0][0] = 0
for _ in range(int(read())):
    a,b = map(int,read().split())
    check[a-1][b-1] = '*'

command = list(False for _ in range(10001))
for _ in range(int(read())):
    a,b = read().split()
    command[int(a)]=b

while True:
    direction = check_dir(time,direction)
    N_P = [snake[-1][0]+dx[direction],snake[-1][1]+dy[direction]]

    if check_way(): time+=1
    else: break

print(time+1)