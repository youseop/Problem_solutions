import sys
read = sys.stdin.readline

n = int(read())
num = list(int(read()) for _ in range(n))
num.sort()

cnt = 1

for i in range(n-1):
    for j in range(i+1, n):
        if num[j]-num[i] >= 5:
            break
        cnt = max(j-i+1, cnt)


if cnt > 4:
    print(0)
else:
    print(5-cnt)
