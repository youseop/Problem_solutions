import sys
n = int(input())
number = list(map(int, sys.stdin.readline().split()))
print(*number)

order = list(0 for _ in range(n))
order[0] = 1

for i in range(1, n):
    for j in range(i):
        if number[j] < number[i] and order[j] > order[i]:
            order[i] = order[j]
    order[i] += 1

print(max(order))
'''
import sys
n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))

arr=list(0 for _ in range(1001))
for num in numbers:
    arr[num]=max(arr[:num])+1

print(max(arr))
'''
