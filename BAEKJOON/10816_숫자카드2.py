import sys
read = sys.stdin.readline

_ = int(read())
tmp1 = list(map(int, read().split()))
_ = int(read())
tmp2 = list(map(int, read().split()))

num = dict()

for i in tmp1:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
answer = []
for i in tmp2:
    if i in num:
        answer.append(num[i])
    else:
        answer.append(0)
print(*answer)
