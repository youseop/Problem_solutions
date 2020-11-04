import sys
read = sys.stdin.readline

n, d, k, c = map(int, read().split())
num = list(int(read()) for _ in range(n))

num = num+num[:k]
check = list(0 for _ in range(d+1))
check[c] = 1
l, r = 0, k-1
count = 0

for i in num[l:r+1]:
    check[i] += 1
    if check[i] == 1:
        count += 1

answer = count
while True:
    check[num[l]] -= 1
    if check[num[l]] == 0:
        count -= 1
    l += 1
    r += 1
    if r == n+k-1:
        break
    check[num[r]] += 1
    if check[num[r]] == 1:
        count += 1
    answer = max(answer, count)

print(answer+1)
