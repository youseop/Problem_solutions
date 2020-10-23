import sys
read = sys.stdin.readline

n, m = map(int, read().split())

friends = dict()
for _ in range(m):
    a, b = map(int, read().split())
    if a in friends:
        friends[a].append(b)
    else:
        friends[a] = [b]
    if b in friends:
        friends[b].append(a)
    else:
        friends[b] = [a]

check = list(0 for _ in range(n))

cnt = 0
# cnt를 사용하지 않고, check배열의 1의 개수로
# 문제의 조건을 판단하면 시간초과가 발생했다.


def dfs(x):
    global cnt
    check[x] = 1
    cnt += 1
    if cnt == 5:  # 깊이가 5 >> ABCDE를 만족하는 친구들이 존재한다는 뜻이다.
        print(1)
        sys.exit()

    for i in friends[x]:
        if check[i] == 0:
            dfs(i)
    cnt -= 1
    check[x] = 0


for i in range(n):
    dfs(i)
# 종료되지 않고 여기까지 넘어오면 ABCDE를 만족하는 친구들이 존재하지 않는다는 뜻이다.
print(0)
