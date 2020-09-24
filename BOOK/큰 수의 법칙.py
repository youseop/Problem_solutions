import sys
sys.stdin = open('input.txt', 'rt')

n, m, k = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
sum, cnt = 0, 0
num.sort()
for _ in range(m):
    if cnt == k:
        cnt = 0
        sum += num[-2]
    else:
        sum += num[-1]
        cnt += 1
print(sum)
