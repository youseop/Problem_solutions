import sys
read = sys.stdin.readline

n, m = map(int, read().split())
num = list(map(int, read().split()))
num.sort()

answer = []


def DFS(cnt, numbs):
    if cnt == m:
        tmp = list(num[i] for i in numbs)
        # if tmp not in answer:
        answer.append(tmp)
        return
    same = 0
    for i in range(n):
        if check[i] and same != num[i]:
            check[i] = False
            DFS(cnt+1, numbs+[i])
            check[i] = True
            same = num[i]


check = list(True for _ in range(n))
DFS(0, [])
for a in answer:
    print(*a)
