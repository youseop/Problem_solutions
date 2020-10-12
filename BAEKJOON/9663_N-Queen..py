import sys
read = sys.stdin.readline

n = int(input())

answer = 0


def bfs(left, center, right):
    global answer
    if len(center) == n:
        answer += 1
        return

    for i in range(len(center)):
        left[i] -= 1
        right[i] += 1

    for i in range(n):
        if i not in left and i not in center and i not in right:
            bfs(left+[i], center+[i], right+[i])
    return


bfs([], [], [])
print(answer)
