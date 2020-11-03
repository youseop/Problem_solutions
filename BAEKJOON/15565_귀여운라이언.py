import sys
read = sys.stdin.readline

n, k = map(int, read().split())
if k == 0:
    print(0)
    sys.exit()
num = list(map(int, read().split()))

l, r, cnt = 0, 0, 0

for i in range(n):
    if num[i] == 1:
        l = i
        break
tmp = 0
for i in range(i, n+1):
    if i == n:
        print(-1)
        sys.exit()
    if num[i] == 1:
        tmp += 1
    if tmp == k:
        r = i
        break

answer = r-l+1
flag = 1
while flag == 1:
    for i in range(l+1, n):
        if num[i] == 1:
            l = i
            break
    for i in range(r+1, n+1):
        if i == n:
            flag = 2
            break
        if num[i] == 1:
            r = i
            break
    if flag == 1:
        answer = min(answer, r-l+1)

if answer < 2147000000:
    print(answer)
else:
    print(-1)
