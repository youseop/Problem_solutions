import sys
n = int(input())
number = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

number.sort(key=lambda x: x[0])

bnum = []
for i in number:
    bnum.append(i[1])

dp = [0]*(max(bnum)+1)

for i in bnum:
    dp[i] = max(dp[:i])+1

print(n-max(dp))
