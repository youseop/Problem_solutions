import sys
read=sys.stdin.readline

def dfs(left, center, right,cnt):
    global answer
    if cnt== n:
        answer += 2
        return
    left  >>= 1
    right <<= 1
    board = center | right | left
    if board&full==full:
        return
    if cnt ==0:
        for i in range(n//2):
            bit = 1 << i
            if not(board & bit):
                dfs(left | bit , center | bit , right | bit , cnt+1)
        return
    for i in range(n):
        bit = 1 << i
        
        if not(board & bit):
            dfs(left | bit , center | bit , right | bit , cnt+1)
    return

def dfs_odd(left, center, right,cnt):
    global answer
    if cnt== n:
        answer += 1
        return
    left  >>= 1
    right <<= 1
    board = center | right | left
    if board&full==full:
        return
    if cnt ==0:
        bit = 1 << (n//2)
        if not(board & bit):
            dfs_odd(left | bit , center | bit , right | bit , cnt+1)
        return
    for i in range(n):
        bit = 1 << i
        
        if not(board & bit):
            dfs_odd(left | bit , center | bit , right | bit , cnt+1)
    return

answer = 0
n = int(input())
full = (1<<n)-1
dfs(0,0,0,0)

if n%2 != 0:
    dfs_odd(0,0,0,0)
print(answer)

