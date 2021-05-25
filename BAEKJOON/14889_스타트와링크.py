import sys
sys.stdin = open("text.txt","rt")
read = sys.stdin.readline


def getDiff(team_a):
    team_b = mask - team_a
    res = 0
    team_a = list(team_a)
    team_b = list(team_b)
    for i in range(n//2):
        for j in range(i+1,n//2):
            a1,a2 = team_a[i],team_a[j]
            b1,b2 = team_b[i],team_b[j]
            res += (status[a1][a2]+status[a2][a1])
            res -= (status[b1][b2]+status[b2][b1])
    return abs(res)


def dfs(team_a,index):
    global min_diff
    if len(team_a) == n//2:
        min_diff = min(min_diff,getDiff(team_a))
        return

    for i in range(index,n):
        dfs(team_a|set([i]),i+1)


n = int(read())
mask = set(i for i in range(n))
status = list(list(map(int,read().split())) for _ in range(n))
min_diff = sys.maxsize

dfs(set(),0)

print(min_diff)