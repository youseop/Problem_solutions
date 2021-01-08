import sys
read=sys.stdin.readline

n = int(read())
rope = list(int(read()) for _ in range(n))
rope.sort(reverse = True)
mw=rope[0]
minimum = rope[0]
for i in range(1,n):
    minimum = min(minimum, rope[i])
    mw = max(mw, minimum*(i+1))

print(mw)

