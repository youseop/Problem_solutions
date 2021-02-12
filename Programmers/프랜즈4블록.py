import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

from collections import deque

def solution(n, m, board):

    def isRec(a,b):
        if board[a][b] == '.':
            return False

        char = board[a][b]
        
        if a+1<n and b+1<m and all(board[i][j] == char for i,j in [(a,b+1),(a+1,b),(a+1,b+1)]):
            return True

        return False


    def delBlock():
        nonlocal answer
        target = [-1,-1]
        for i in range(n):
            for j in range(m):
                if board[i][j] != '.' and isRec(i,j):
                    target = [i,j]
                    break
            if target[0] != -1:
                break
        if target[0] == -1:
            return 0

        point = deque([])
        point.append([target[0]+1,target[1]])
        point.append([target[0],target[1]+1])
        point.append([target[0]+1,target[1]+1])

        visit = list(list(1 for _ in range(m))for _ in range(n))
        for i in range(2):
            for j in range(2):
                visit[target[0]+i][target[1]+j] = 0

        while point:
            a,b = point.popleft()
            if isRec(a,b):
                for i in range(2):
                    for j in range(2):
                        if visit[a+i][b+j]:
                            point.append([a+i,b+j])
                            visit[a+i][b+j] = 0

        point = deque([[target[0],target[1]]])
        board[target[0]][target[1]] = '.'
        visit[target[0]][target[1]] = 1
        while point:
            a,b = point.popleft()
            answer += 1
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                ax,by = a+x,b+y
                if 0<=ax<n and 0<=by<m and visit[ax][by] == 0:
                    board[ax][by] = '.'
                    visit[ax][by] = 1
                    point.append([ax,by])

        return 1

    def drop():
        flag = 1
        for j in range(m):
            drop = 0
            drop_cnt = 0
            for i in range(n-1,-1,-1):
                if board[i][j] == '.':
                    drop = 1
                elif drop:
                    flag = 0
                    board[i+drop_cnt][j] = board[i][j]
                    board[i][j] = '.'
                    drop_cnt -= 1
                if drop:
                    drop_cnt += 1
        return flag

    answer = 0
    board = list(list(b) for b in board)
    while 1:
        while 1:
            if not delBlock():
                break
        if drop():
            break
     
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
#14
#15
