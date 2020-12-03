
import sys
read = sys.stdin.readline

n, c = map(int, read().split())
m = int(read())
things = list(list(map(int, read().split())) for _ in range(m))
# 물건의 도착지가 빠른 순으로 정렬
things.sort(key=lambda x: (x[1], x[0]))
# 해당 마을에서 물건을 얼마나 더 실을 수 있는지 확인
left = list(c for _ in range(n+1))

answer = 0

for a, b, w in things:
    # a ~ b마을에서 물건을 더 실을 수 있는 값들의 최소값
    available = min(left[a:b])
    if available > 0:
        put = min(available, w)
        answer += put
        for i in range(a, b):
            left[i] -= put
print(answer)
