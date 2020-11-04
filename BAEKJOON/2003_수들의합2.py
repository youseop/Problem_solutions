import sys
read = sys.stdin.readline

n, m = map(int, read().split())
num = list(map(int, read().split()))

l, r = 0, 0
answer = 0
sum_num = num[0]
while r != n:
    while r != n:
        if sum_num == m:
            answer += 1
            sum_num -= num[l]
            l += 1
            break
        elif sum(num[l:r+1]) > m:
            sum_num -= num[l]
            l += 1
            break
        else:
            r += 1
            if r == n:
                break
            sum_num += num[r]
print(answer)
