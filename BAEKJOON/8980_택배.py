import sys
read = sys.stdin.readline

n, c = map(int, read().split())
m = int(read())
things = list(list(map(int, read().split())) for _ in range(m))
things.sort(key=lambda x: (x[1], x[0]))

left = list(c for _ in range(n+1))
answer = 0
for a, b, w in things:
    available = min(left[a:b])
    if available > 0:
        put = min(available, w)
        answer += put
        for i in range(a, b):
            left[i] -= put
print(answer)
