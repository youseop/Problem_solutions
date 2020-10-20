import sys
sys.stdin = open("input.txt", "rt")
read = sys.stdin.readline

N = int(read())
lines = list(list(map(int, read().split())) for _ in range(N))
num = []
lines.sort()
for a, b in lines:
    num.append(b)
give_start = dict()
for a, b in lines:
    give_start[b] = a


dp = [num[0]]
check = list(0 for _ in range(N))
check[0] = 1


def bin_search(x):
    a = 0
    b = len(dp)-1
    while a <= b:
        mid = (a+b)//2
        if dp[mid] > x:
            if 0 <= mid-1 and dp[mid-1] < x:
                dp[mid] = x
                check[i] = mid+1
                break
            elif dp[0] > x:
                dp[0] = x
                check[i] = 1
                break
            else:
                b = mid-1
        else:
            a = mid+1


for i in range(1, N):
    n = num[i]
    if n > dp[-1]:
        dp.append(n)
        check[i] = len(dp)
    else:
        bin_search(n)

# print(dp)
print(N-len(dp))
# print(num)
# print(check)

cnt = len(dp)
semi_answer = []
for i in range(N-1, -1, -1):
    if check[i] == cnt:
        cnt -= 1
        semi_answer.append(num[i])

# print(semi_answer)
num = set(num)
semi_answer = set(semi_answer)
num -= semi_answer
num = list(num)
answer = []
for n in num:
    answer.append(give_start[n])
answer.sort()
for a in answer:
    print(a)
