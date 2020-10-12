import sys
read = sys.stdin.readline

n = int(input())
num = list(int(read()) for _ in range(n))


def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x


for i in range(n-1):
    num[i] = abs(num[i+1]-num[i])
num.pop()

tmp = num[0]
for x in num:
    tmp = GCD(tmp, x)

answer = set([tmp])
for i in range(2, 1+int(tmp**(1/2))):
    if tmp % i == 0:
        answer.add(i)
        answer.add(tmp//i)

answer = list(answer)
answer.sort()
print(*answer)
