import sys
n = int(input())
number = list(map(int, sys.stdin.readline().split()))
# 증가하는 수열 최대길이 _왼쪽부터
order_left = list(0 for _ in range(n))
order_left[0] = 1

for i in range(1, n):
    for j in range(i):
        if number[j] < number[i] and order_left[j] > order_left[i]:
            order_left[i] = order_left[j]
    order_left[i] += 1

order_right = list(0 for _ in range(n))
order_right[0] = 1
# 증가하는 수열 최대길이 _오른쪽부터
number = number[::-1]

for i in range(1, n):
    for j in range(i):
        if number[j] < number[i] and order_right[j] > order_right[i]:
            order_right[i] = order_right[j]
    order_right[i] += 1
order_right = order_right[::-1]
# 합친 후 i자리의 숫자가 두번들어가 겹침으로 1을 뺀다.
answer = 0  # 최대값 저장
for i in range(n):
    tmp = order_right[i]+order_left[i]-1
    if tmp > answer:
        answer = tmp
print(answer)
