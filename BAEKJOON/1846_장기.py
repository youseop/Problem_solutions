import sys
n = int(input())

if n == 3:
    print(-1)
    sys.exit()
if n % 2 == 0:
    cnt = 1
    for i in range(n):
        if i == n//2:
            print(1)
        elif i == n//2-1:
            print(n)
        else:
            cnt += 1
            print(cnt)
else:
    cnt = 1
    for i in range(n):
        if i == n//2:
            print(1)
        elif i == n//2-1:
            print(n)
        else:
            cnt += 1
            print(cnt)
