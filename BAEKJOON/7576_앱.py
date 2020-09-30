import sys
n, m = map(int, sys.stdin.readline().split())
apps = list(map(int, sys.stdin.readline().split()))
memorys = list(map(int, sys.stdin.readline().split()))

k = sum(memorys)+1

kill = list(0 for _ in range(k+1))
for app, memory in zip(apps, memorys):
    for j in range(k-memory, -1, -1):
        kill[j+memory] = max(app+kill[j], kill[j+memory])
    print(kill)
for index, val in enumerate(kill):
    if val >= m:
        print(index)
        break
