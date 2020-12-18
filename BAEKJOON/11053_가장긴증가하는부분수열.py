import sys
read=sys.stdin.readline

def lower_bound(n):
    l,r = 0,answer_len
    while l<=r:
        mid = (l+r)//2
        if answer[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
            save = mid
    answer[save] = n

N=int(read())
num=list(map(int,read().split()))

answer = [num[0]]

answer_len=1
for n in num[1:]:
    if n > answer[-1]: 
        answer.append(n)
        answer_len += 1
    if n < answer[-1]: lower_bound(n)

print(len(answer))